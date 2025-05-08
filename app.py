from flask import Flask, render_template, request
import os
import speech_recognition as sr
from pydub import AudioSegment

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', output_text=None)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=None)
        print("Processing...")

    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could not understand audio."
    except sr.RequestError:
        text = "Speech recognition service unavailable."

    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', output_text="No file uploaded.")

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    if filepath.endswith('.mp3'):
        audio = AudioSegment.from_mp3(filepath)
        filepath = filepath.replace('.mp3', '.wav')
        audio.export(filepath, format='wav')

    recognizer = sr.Recognizer()

    with sr.AudioFile(filepath) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
    except:
        text = "Could not recognize speech."

    return render_template('index.html', output_text=text)

if __name__ == '__main__':
    app.run(debug=True)
