# 🎙️ AI-Powered Audio Enhancement & Transcription

This is a comprehensive **audio enhancement and transcription framework** that combines noise reduction, silence removal, and AI-powered speech-to-text conversion. Built using Python, AssemblyAI, Librosa, Noisereduce, and PyAudioAnalysis, this project provides a highly automated pipeline for enhancing poor quality audio and converting speech into text, applicable in law enforcement, forensic analysis, and research.

---

## 📌 Project Objectives

- Enhance audio quality through noise reduction and silence removal
- Convert multi-format audio/video files into clean `.wav` format
- Transcribe speech using AI-powered speech-to-text APIs
- Generate accurate transcripts for legal, forensic, or research applications
- Handle real-world audio challenges: background noise, overlapping speech, static, and varied environments

---

## 🛠️ Tech Stack & Tools

| Tool | Purpose |
|------|---------|
| 🐍 Python 3.9+ | Core programming language |
| 🎙️ AssemblyAI | Speech-to-text transcription |
| 📊 Librosa | Audio analysis & signal processing |
| 🔇 Noisereduce | Noise reduction |
| 🔎 PyAudioAnalysis | Silence removal & audio segmentation |
| 🎞️ MoviePy | Video to audio extraction |
| 🎧 Pydub | Audio format conversion |
| 📈 NumPy & SciPy | Scientific computing |
| 📂 SoundFile | Audio file I/O |

---

## 📦 Prerequisites

- Python 3.9+
- FFmpeg installed (for video/audio conversion)
- AssemblyAI account with valid API key
- Minimum 4GB RAM (recommended 8GB+ for large files)
- Works on Windows, Linux, and macOS

---

## ⚙️ Setup & Installation

👉 Follow the full [Setup Guide](SETUP.md) for step-by-step installation and configuration.

---

## 📁 Repository Contents

| Folder/File | Description |
|-------------|-------------|
| `input/` | Input folder for raw video/audio files |
| `enhanced/` | Enhanced audio files |
| `transcripts/` | Generated transcription text files |
| `convert_to_wav.py` | Convert various formats to WAV |
| `audio_enhancement.py` | Perform noise reduction & enhancement |
| `audio_transcription.py` | Upload to AssemblyAI and transcribe |
| `API_secrets.py` | Store your AssemblyAI API key |
| `requirements.txt` | Python dependencies |
| `SETUP.md` | Complete setup instructions |
| `README.md` | Project documentation |

---

## 🔍 Example Output

**Sample File:** noisy_audio_sample.mp4  
**Enhanced Output:** noise-free_sample.wav  
**Transcription Output:**

> "This is the transcribed text after audio enhancement using AssemblyAI..."

**Noise Reduction Applied:**

- Spectral noise gating (Librosa + Noisereduce)
- Silence segment trimming (PyAudioAnalysis)

**Average Word Error Rate (WER):**

> ~0% to 10% depending on noise conditions

---

## 📈 Key Results

- Clear audio obtained from noisy environments (crowded rooms, traffic, construction, wind)
- Consistent transcription accuracy across devices (iOS & Android)
- Demonstrated applicability for forensic & legal audio analysis

---

## 🚀 Future Enhancements

- 🗣️ Add speaker diarization (multi-speaker identification)
- 🌐 Language identification for multilingual transcription
- 📊 Build interactive GUI interface for end-users
- 🧠 Develop AI-based adaptive noise profiles for forensic analysis
- 📅 Automate complete end-to-end batch processing

---

## 📄 License

MIT License

---

## 👤 Author

**Gokul Parandhaman**

MSc Information Security @ Royal Holloway, University of London

📧 gokulparandhaman1015@gmail.com

[LinkedIn](https://www.linkedin.com)

