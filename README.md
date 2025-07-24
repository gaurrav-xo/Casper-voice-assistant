
🎙️ Casper – Python Voice Assistant

"Casper" is a simple, offline-friendly voice assistant built with Python. It responds to your voice, performs web actions, plays music from a custom library, and answers your questions using Wikipedia.

---

✨ Features

- 🗣️ Wake word detection (`"casper"`)
- 🔊 Text-to-speech responses using `pyttsx3`
- 🌐 Opens websites like Google, YouTube, Facebook, and Instagram
- 🎵 Plays music via URLs from a custom `musiclibrary.py`
- 📚 Answers general knowledge questions using Wikipedia
- 🛑 Exits gracefully on voice command

---

🛠️ Tech Stack

- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – Voice-to-text
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – Text-to-speech
- [`wikipedia`](https://pypi.org/project/wikipedia/) – Wikipedia search integration
- `webbrowser` – Built-in Python module for URL actions
- `musiclibrary` – Custom module storing music names & links



🚀 Getting Started

📋 Requirements

- Python 3.7 or later
- Microphone (for voice input)
- Internet connection (for speech recognition and Wikipedia)

⚙️ Installation

1. Clone this repository

   bash
   git clone https://github.com/gaurrav-xo/Casper-voice-assistant.git
   cd Casper-voice-assistant


2. Install dependencies

   bash
   pip install -r requirements.txt
   

3. Add a `musiclibrary.py` file** (same folder as `casper.py`)

   python
   # musiclibrary.py
   music = {
       "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
       "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
       # Add more songs as needed
   }
   

4. Run the assistant

   bash
   python casper.py
   



🗣️ Voice Commands

| Command                | Action                                |
| ---------------------- | ------------------------------------- |
| `Casper`               | Wakes the assistant                   |
| `Open Google`          | Opens Google in the browser           |
| `Play faded`           | Plays "faded" from your music library |
| `Tell me about Python` | Reads a short Wikipedia summary       |
| `Who is Elon Musk`     | Answers using Wikipedia               |
| `Exit`                 | Closes the assistant                  |



📁 File Structure


Casper-voice-assistant/
├── casper.py
├── musiclibrary.py
├── requirements.txt
└── README.md




👤 Author
   
   Gaurrav
🔗 [@gaurrav-xo](https://github.com/gaurrav-xo)



📄 License

This project is licensed under the [MIT License](LICENSE).


