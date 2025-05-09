````markdown
# 🎤 SpeechRecognitionApp

A web-based Speech-to-Text application built with Python and Flask that enables real-time voice transcription and audio file upload functionality. It uses the `speech_recognition` library to convert spoken words into text, either from live microphone input or uploaded `.mp3`/`.wav` files.

---

## 🚀 Features

- 🎙️ **Real-Time Speech Recognition**  
  Press a button to start speaking and transcribe your voice into text automatically.

- 📁 **Audio File Upload Support**  
  Upload `.mp3` or `.wav` files to convert recorded speech into text.

- ⏱️ **Automatic Stop on Silence**  
  The recording ends automatically after detecting a period of silence—no manual stop required.

- 💬 **Clear and Responsive UI**  
  An attractive and simple user interface using HTML, CSS, and Font Awesome icons.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (minimal)
- **Backend**: Python 3, Flask
- **Libraries**:
  - [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
  - [`pydub`](https://pypi.org/project/pydub/)
  - `ffmpeg` (system-level requirement for handling MP3 files)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Anishkumar-1804/SpeechRecognitionApp.git
cd SpeechRecognitionApp
````

### 2. Install Python Dependencies

Make sure you’re using Python 3.6+.

```bash
pip install flask SpeechRecognition pydub
```

### 3. Install ffmpeg (Required by `pydub`)

* **Windows**:
  Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your system PATH.

* **Linux**:

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

---

## ▶️ Run the App

```bash
python app.py
```

Open your browser and go to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Structure

```
SpeechRecognitionApp/
│
├── static/
│   └── script.js           # Frontend JavaScript for handling UI interactions
│
├── templates/
│   └── index.html          # Main web interface
│
├── app.py                  # Flask backend application
├── README.md               # Project documentation
```

---

## 📌 Usage

* Click **Start Recording** to begin transcribing your voice.
* Wait until the system detects silence to automatically stop and display the text.
* Or, upload an audio file (`.mp3` or `.wav`) and let it transcribe automatically.
* The final output will appear in the **Transcription** section.

---

## 👨‍💻 Author

Anishkumar K
GitHub: [Anishkumar-1804](https://github.com/Anishkumar-1804)

---

## 📜 License

This project is open-source and free to use for educational or personal projects.

---

## 💡 Future Improvements

* Add language selection (multilingual support)
* Enhance recognition accuracy using advanced models (like Whisper or DeepSpeech)
* Mobile-friendly UI

---

```
```
