
from flask import Flask, request
from flask_cors import CORS
# import voiceToText2
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        # save_path = f"./uploads/{file.filename}"
        file.save(save_path)
        print(save_path)
        res = audio_to_text(save_path)
        print(res)
        return res, 200


import speech_recognition as sr
from rake_nltk import Rake
import nltk
from pydub import AudioSegment
import google.generativeai as genai
import textwrap
from IPython.display import display
from IPython.display import Markdown
# nltk.download('stopwords')
# nltk.download('punkt')

genai.configure(api_key="AIzaSyAomvNpnBZHa9LV3Vkw7qHPiyH7yJYkfg4")
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def convert_to_wav(input_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Extract the file name without extension
    file_name = os.path.splitext(input_file)[0]

    # Define the output file name
    output_file = file_name + ".wav"

    # Export the audio file in .wav format
    audio.export(output_file, format="wav")

    print(f"File converted and saved as output_file")
    return output_file

def audio_to_text(audio_file):
    input_file = audio_file
    audio_file2 = convert_to_wav(input_file)
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file2) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    res = "Extracted Text:", text.capitalize()
    strng = "Classify this data " + text
    response = model.generate_content(strng)
    res2 = response.text
    return res + res2

if __name__ == '__main__':
    app.run(debug=True)
