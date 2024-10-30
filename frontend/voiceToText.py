# # import openai
# # import speech_recognition as sr

# # # Your Gemini API Key
# # openai.api_key = 

# # # Initialize speech recognizer
# # r = sr.Recognizer()

# # # Record audio from microphone
# # with sr.Microphone() as source:
# #     print("Speak now...")
# #     audio = r.listen(source)

# # try:
# #     text = r.recognize_google(audio)
# #     print(f"You said: {text}")

# #     # Use Gemini for summarization (make sure to use the correct model name)
# #     response = openai.ChatCompletion.create(
# #         model="Gemini 1.5 Flash",  # Replace with the correct Gemini model name
# #         messages=[
# #             {"role": "user", "content": f"Summarize this text:\n\n{text}"}
# #         ],
# #         temperature=0.5,  # Controls creativity (0-1)
# #     )

# #     summary = response.choices[0].message.content.strip()
# #     print(f"Summary: {summary}")

# # except sr.UnknownValueError:
# #     print("Could not understand audio")
# # except sr.RequestError as e:
# #     print(f"Could not request results from Google Speech Recognition; {e}")



# # pip install speechrecognition
# # pip install PyAudio
# # pip install pyttsx3

# # import speech_recognition as sr
# # import pyttsx3

# # r=sr.Recognizer()

# # def record_text():
# #   while(1):

# #     try:
# #       with sr.Microphone() as source2:
# #         r.adjust_for_ambient_noise(source2, duration=0.2)
# #         audio2 = r.listen(source2)
# #         MyText = r.recognize_google(audio2)
# #         return MyText


# #     except sr.RequestError as e:
# #       print("Could not request results; {0}".format(e))
# #     except sr.UnknownValueError:
# #       print("Unknown error occured")
# #   return


# # with sr.Microphone() as source:
# #     print("Say something!")
# #     audio = r.listen(source)


# # import speech_recognition as sr
# # import pyttsx3
# # from transformers import pipeline
# # # import openai


# # # openai.api_key =  

# # # Initialize the recognizer
# # r = sr.Recognizer()

# # # Initialize text-to-speech engine
# # engine = pyttsx3.init()

# # def record_text():
# #     while True:
# #         try:
# #             with sr.Microphone() as source2:
# #                 r.adjust_for_ambient_noise(source2, duration=0.2)
# #                 print("Listening...")
# #                 audio2 = r.listen(source2)
# #                 MyText = r.recognize_google(audio2)
# #                 MyText = MyText.capitalize()
                
# #                 print(f"You said: {MyText}")
                
# #                 # Speak the recognized text
# #                 engine.say(MyText)
# #                 engine.runAndWait()
                
# #                 return MyText

# #         except sr.RequestError as e:
# #             print("Could not request results; {0}".format(e))
# #         except sr.UnknownValueError:
# #             print("Unknown error occurred. Please try again.")

# # # def summarize_text(text):
# # #     summarizer = pipeline("summarization")
# # #     summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
# # #     return summary[0]['summary_text']

# # # Start listening and processing speech
# # if __name__ == "__main__":
# #     with sr.Microphone() as source:
# #         print("Say something!")
# #         audio = r.listen(source)
# #     MyText = record_text()
#     # if record_text:
#     #         # Step 2: Summarize the text
#     #         summarized_text = summarize_text(MyText)

# #     response = openai.ChatCompletion.create(
# #     model="gpt-4",  # Replace with the correct Gemini model name
# #     messages=[
# #         {"role": "user", "content": f"Summarize this text:\n\n{MyText}"}
# #     ],
# #     temperature=0.5,  # Controls creativity (0-1)
# # )

# # summary = response.choices[0].message.content.strip()
# # print(f"Summary: {summary}")
#     # print (MyText)


# # import speech_recognition as sr
# # import pyttsx3
# # from transformers import pipeline
# # from google.generative_ai import TextGenerationModel

# # # Initialize the recognizer
# # r = sr.Recognizer()

# # # Initialize text-to-speech engine
# # engine = pyttsx3.init()

# # def record_text():
# #     while True:
# #         try:
# #             with sr.Microphone() as source2:
# #                 r.adjust_for_ambient_noise(source2, duration=0.2)
# #                 print("Listening...")
# #                 audio2 = r.listen(source2)
# #                 MyText = r.recognize_google(audio2)
# #                 MyText = MyText.capitalize()
                
# #                 print(f"You said: {MyText}")
                
# #                 # Speak the recognized text
# #                 engine.say(MyText)
# #                 engine.runAndWait()
                
# #                 return MyText

# #         except sr.RequestError as e:
# #             print("Could not request results; {0}".format(e))
# #         except sr.UnknownValueError:
# #             print("Unknown error occurred. Please try again.")

# # def summarize_text(text):
# #     # Gemini API endpoint
# #     url = "https://api.gemini.google.com/v1/models/gemini-1.5-flash/generate"  # Replace with actual Gemini API endpoint
# #     api_key =   # Replace with your Gemini API key
    
# #     headers = {
# #         "Authorization": f"Bearer {api_key}",
# #         "Content-Type": "application/json"
# #     }
    
# #     data = {
# #         "text": text,
# #         "length": "short"  # You can adjust the length parameter to 'short', 'medium', or 'long'
# #     }
    
# #     response = requests.post(url, json=data, headers=headers)
    
# #     if response.status_code == 200:
# #         summary = response.json().get("summary")
# #         print(f"Summary: {summary}")
# #         return summary
# #     else:
# #         print(f"Failed to summarize text: {response.status_code}")
# #         return None

# # # Start listening and processing speech
# # if __name__ == "__main__":
# #     MyText = record_text()
# #     summary = summarize_text(MyText)
    
# #     if summary:
# #         # Speak the summarized text
# #         engine.say(summary)
# #         engine.runAndWait()






# #WORKS

# # import speech_recognition as sr
# # import pyttsx3
# # from transformers import pipeline
# # from google.generativeai import TextGenerationModel

# # # Initialize the recognizer
# # r = sr.Recognizer()

# # # Initialize text-to-speech engine
# # engine = pyttsx3.init()

# # # def summarize_text(text):
# # #     # Replace 'YOUR_API_KEY' with your actual Gemini API key
# # #     model = TextGenerationModel(api_key=)

# # #     # Set the prompt for text summarization
# # #     prompt = f"Summarize this text: {text}"

# # #     # Generate a summary using the Gemini model
# # #     summary = model.generate(prompt=prompt)

# # #     return summary

# # def record_text():
# #     while True:
# #         try:
# #             with sr.Microphone() as source2:
# #                 r.adjust_for_ambient_noise(source2, duration=0.2)
# #                 print("Listening...")
# #                 audio2 = r.listen(source2)
# #                 MyText = r.recognize_google(audio2)
# #                 MyText = MyText.capitalize()
                
# #                 print(f"You said: {MyText}")
                
# #                 # Speak the recognized text
# #                 engine.say(MyText)
# #                 engine.runAndWait()
                
# #                 return MyText

# #         except sr.RequestError as e:
# #             print("Could not request results; {0}".format(e))
# #         except sr.UnknownValueError:
# #             print("Unknown error occurred. Please try again.")


# # # Start listening and processing speech
# # if __name__ == "__main__":
# #     with sr.Microphone() as source:
# #         print("Say something!")
# #         audio = r.listen(source)
# #     MyText = record_text()

# #WORKS






# # summary = summarize_text(MyText)
# # print("Summary:", summary)

# # # Speak the summary
# # engine.say(summary)
# # engine.runAndWait()



# from flask import Flask, request, jsonify
# import speech_recognition as sr
# import pyttsx3
# from flask_cors import CORS

# # Initialize Flask app
# app = Flask(__name__)

# CORS(app)

# # Initialize the recognizer and text-to-speech engine
# r = sr.Recognizer()
# engine = pyttsx3.init()

# # @app.route('/upload', methods=['POST'])
# # def upload_audio():
# #     if 'audio' not in request.files:
# #         return jsonify({'error': 'No audio file in request'}), 400

# #     audio_file = request.files['audio']
    
# #     # Save the file temporarily
# #     file_path = 'uploaded_recording.ogg'
# #     audio_file.save(file_path)

# #     # Process the audio file
# #     text = process_audio(file_path)

# #     # Optionally, convert the recognized text to speech
# #     engine.say(text)
# #     engine.runAndWait()

# #     return jsonify({'recognized_text': text}), 200

# @app.route('/upload', methods=['POST'])
# def upload_audio():
#     try:
#         if 'audio' not in request.files:
#             return jsonify({'error': 'No audio file in request'}), 400

#         audio_file = request.files['audio']

#         # Save the file temporarily
#         file_path = 'uploaded_recording.ogg'
#         audio_file.save(file_path)

#         # Process the audio file and recognize the text
#         text = process_audio(file_path)

#         # Optionally, convert the recognized text to speech
#         engine.say(text)
#         engine.runAndWait()

#         # Return the recognized text to the frontend
#         return jsonify({'recognized_text': text}), 200

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


# def process_audio(file_path):
#     # Load the audio file and recognize the speech
#     with sr.AudioFile(file_path) as source:
#         audio = r.record(source)
#         try:
#             text = r.recognize_google(audio)
#             text = text.capitalize()
#             print(f"Recognized text: {text}")
#             return text
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#             return "RequestError"
#         except sr.UnknownValueError:
#             print("Could not understand the audio")
#             return "UnknownValueError"

# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment

app = Flask(__name__)
CORS(app)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file in request'}), 400

        audio_file = request.files['audio']

        # Save the OGG file temporarily
        ogg_path = 'uploaded_recording.ogg'
        audio_file.save(ogg_path)

        # Convert OGG to WAV
        wav_path = 'uploaded_recording.wav'
        audio = AudioSegment.from_ogg(ogg_path)
        audio.export(wav_path, format='wav')

        # Process the WAV file and recognize the text
        text = process_audio(wav_path)

        # Optionally, convert the recognized text to speech
        engine.say(text)
        engine.runAndWait()

        return jsonify({'recognized_text': text}), 200

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

def process_audio(file_path):
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            text = text.capitalize()
            print(f"Recognized text: {text}")
            return text
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "RequestError"
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return "UnknownValueError"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
