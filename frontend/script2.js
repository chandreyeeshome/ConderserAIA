// Access the microphone and start recording
async function startRecording() {
    const button = document.getElementById('start');
    button.classList.toggle('clicked');
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    const audioChunks = [];

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        document.getElementById('player').src = audioUrl;

        // Send the recorded audio to the Python backend
        const formData = new FormData();
        formData.append('file', audioBlob, 'recording.wav');

        try {
            const response = await fetch('http://127.0.0.1:5000/upload', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                console.log('File uploaded successfully');
            } else {
                console.error('Failed to upload file');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    mediaRecorder.start();

    // Stop recording after 5 seconds or use a stop button
    document.getElementById('stop').onclick = () => {
        mediaRecorder.stop();
        stream.getTracks().forEach(track => track.stop());
    };
}

// Attach the startRecording function to the start button
document.getElementById('start').onclick = startRecording;

const showText = () => {
	var text = document.getElementById("containerText")
	// console.log(text)
}
