class VoiceRecorder {
	constructor() {
		if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
			console.log("getUserMedia supported")
		} else {
			console.log("getUserMedia is not supported on your browser!")
		}

		this.mediaRecorder
		this.stream
		this.chunks = []
		this.isRecording = false

		this.recorderRef = document.querySelector("#recorder")
		this.playerRef = document.querySelector("#player")
		this.startRef = document.querySelector("#start")
		this.stopRef = document.querySelector("#stop")
		
		this.startRef.onclick = this.startRecording.bind(this)
		this.stopRef.onclick = this.stopRecording.bind(this)

		this.constraints = {
			audio: true,
			video: false
		}
		
	}

	handleSuccess(stream) {
		this.stream = stream
		this.stream.oninactive = () => {
			console.log("Stream ended!")
		};
		this.recorderRef.srcObject = this.stream
		this.mediaRecorder = new MediaRecorder(this.stream)
		console.log(this.mediaRecorder)
		this.mediaRecorder.ondataavailable = this.onMediaRecorderDataAvailable.bind(this)
		this.mediaRecorder.onstop = this.onMediaRecorderStop.bind(this)
		this.recorderRef.play()
		this.mediaRecorder.start()
	}

	handleError(error) {
		console.log("navigator.getUserMedia error: ", error)
	}
	
	onMediaRecorderDataAvailable(e) { this.chunks.push(e.data) }
	
	// onMediaRecorderStop(e) { 
	// 		const blob = new Blob(this.chunks, { 'type': 'audio/ogg; codecs=opus' })
	// 		const audioURL = window.URL.createObjectURL(blob)
	// 		this.playerRef.src = audioURL
	// 		this.chunks = []
	// 		this.stream.getAudioTracks().forEach(track => track.stop())
	// 		this.stream = null
	// }


	
	// onMediaRecorderStop(e) {
	// 	// Create a Blob from the recorded audio chunks
	// 	const blob = new Blob(this.chunks, { 'type': 'audio/ogg; codecs=opus' });
	// 	const audioURL = window.URL.createObjectURL(blob);
	// 	this.playerRef.src = audioURL;
	// 	this.chunks = [];
	// 	this.stream.getAudioTracks().forEach(track => track.stop());
	// 	this.stream = null;
	
	// 	// Prepare the audio data to be sent to the server
	// 	const formData = new FormData();
	// 	formData.append('audio', blob, 'recording.ogg'); // 'audio' is the form field name, 'recording.ogg' is the filename
	
	// 	// Send the recorded audio to the server
	// 	fetch('http://localhost:5000/upload', {
	// 		method: 'POST',
	// 		body: formData,
	// 	})
	// 	.then(response => response.json())
	// 	.then(data => {
	// 		console.log('Success:', data);
	// 	})
	// 	.catch((error) => {
	// 		console.error('Error:', error);
	// 	});
	// }

	onMediaRecorderStop(e) {
		const blob = new Blob(this.chunks, { 'type': 'audio/ogg; codecs=opus' });
		const audioURL = window.URL.createObjectURL(blob);
		this.playerRef.src = audioURL;
		this.chunks = [];
		this.stream.getAudioTracks().forEach(track => track.stop());
		this.stream = null;
	
		const formData = new FormData();
		formData.append('audio', blob, 'recording.ogg');
	
		fetch('http://localhost:5000/upload', {
			method: 'POST',
			body: formData,
		})
		.then(response => response.json())
		.then(data => {
			console.log('Success:', data);
			// Display the recognized text from the response
			if (data.recognized_text) {
				// For example, display it in an HTML element
				document.querySelector("#containerText").innerText = `Recognized Text: ${data.recognized_text}`;
			}
		})
		.catch((error) => {
			console.error('Error:', error);
		});
	}
	
	

	startRecording() {
		if (this.isRecording) return
		this.isRecording = true
		// this.startRef.innerHTML = 'Recording...'
		this.startRef.style.borderColor = 'white';
		this.startRef.style.borderWidth = '5px';
		this.playerRef.src = ''
		navigator.mediaDevices
			.getUserMedia(this.constraints)
			.then(this.handleSuccess.bind(this))
			.catch(this.handleError.bind(this))
	}
	
	stopRecording() {
		if (!this.isRecording) return
		this.isRecording = false
		// this.startRef.innerHTML = 'Record'
		this.startRef.style.borderColor = '#7f2b86';
		this.startRef.style.borderWidth = '2px';
		this.recorderRef.pause()
		this.mediaRecorder.stop()
	}
	
}

window.voiceRecorder = new VoiceRecorder()

