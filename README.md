# Robert – Voice Assistant 🧠🎙️

**Developed by:** [Huzaifa Abdulrab](https://github.com/Huzaifaabdulrab)  
**Contact:** huzaifaabdulrab@gmail.com

---

### ▶️ More Detail & How to run this project
You see This documentation robert documentation.pdf

---

### 🎯 Introduction

**Robert** is a voice-activated assistant created to help **visually impaired users** interact with their system using voice commands. It allows you to **open websites, search content, play videos**, and much more — all through your voice!

This is a **Command-Line Interface (CLI)** Python project that listens for the trigger word **"Robert"**, and then processes user voice commands using `speech_recognition` and `pyttsx3`.

> 📄 For detailed instructions and command list, please refer to the documentation PDF included in this repository.

---

### 🚀 Features

- Activate using voice: **"Robert"**
- Command: Open websites (e.g., Google, YouTube, Facebook, etc.)
- YouTube: Search and play videos by voice
- Google: Search directly by speaking
- Text-to-speech interaction
- Error handling for background noise or unrecognized commands

---

### 🧠 How it Works

1. **Say "Robert"** to activate the assistant.
2. Speak your command clearly (e.g., "Open Google", "Search YouTube cats").
3. Assistant performs the command and responds through voice.

---

### 🛠 Requirements

- Python 3.x
- A working microphone
- Internet connection
- Quiet environment for accurate detection

---



### ▶️ How to Run

```bash
git clone https://github.com/Huzaifaabdulrab/huzaifa-voice-assistant
cd huzaifa-voice-assistant
pip install SpeechRecognition pyttsx3 pyaudio
python main.py
