import speech_recognition as sr
from rake_nltk import Rake
import nltk
from pydub import AudioSegment
import os
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



# def extract_keywords(text):
#     rake = Rake()
#     rake.extract_keywords_from_text(text)
#     keywords = rake.get_ranked_phrases_with_scores()
#     return keywords



# def generate_tags(keywords, num_tags=5):
#     tags = [keyword[1] for keyword in keywords[:num_tags]]
#     return tags


# Process the audio file
# audio_file = 'test.wav'  
# text = audio_to_text(audio_file)


# keywords = extract_keywords(text)
# tags = generate_tags(keywords)

# print("Extracted Text:", text.capitalize())
# print("Keywords:", keywords)
# print("Suggested Tags:", tags)

# strng = "Classify this data " + text
# response = model.generate_content(strng)

# print(response.text)

# "text"
# : "**Emotion:** Grief, loss, despair, hopelessness\n\n**Theme:**\n* Betrayal and abandonment by loved ones\n* Protecting a cherished object at great personal cost\n* The futility of words in the face of overwhelming loss\n* The concept of impostors or false identities"

# print(to_markdown(response.text))