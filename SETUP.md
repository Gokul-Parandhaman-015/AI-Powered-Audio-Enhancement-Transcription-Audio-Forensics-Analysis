# ⚙️ Setup Guide: AI-Powered Audio Enhancement & Transcription

This setup guide will walk you through step-by-step instructions to install dependencies, configure the project, and run your audio enhancement & transcription pipeline.

---

## 🚀 Project Workflow Overview

The full flow of your project is as follows:

1️⃣ **Input**  
Provide any audio or video file in various formats (`.mp4`, `.avi`, `.mp3`, `.wav`, etc.)

2️⃣ **Video to Audio Conversion**  
Convert video/audio files into clean `.wav` format using `video to audio.py`

3️⃣ **Audio Enhancement**  
Perform noise reduction and silence removal using `AudioEnhancement (1).py`

4️⃣ **Audio Transcription**  
Use `audio_transcription.py`  with AssemblyAI API to transcribe enhanced audio into text

5️⃣ **Output**  
Receive high-quality audio (`enhanced_audio.wav`) and corresponding text transcription file

---

## 📦 Prerequisites

- Python 3.9+ installed  
- FFmpeg installed and added to PATH  
- AssemblyAI account (to get your API key)  
- Minimum 4GB RAM (8GB recommended)

---

## 🖥️ System Requirements

| Component | Requirement |
|-----------|--------------|
| OS | Windows / Linux / macOS |
| Python | 3.9+ |
| Disk Space | 10GB recommended |
| Internet | Required for transcription (API calls) |

---

## 📁 Repository Folder Structure

```bash
audio-enhancement-transcription/
│
├── input/                  # Raw input files (video/audio)
├── enhanced/               # Enhanced audio output
├── transcripts/            # Transcription output
│
├── video to audio.py       # Convert video/audio files into WAV
├── AudioEnhancement (1).py # Enhance WAV files (noise reduction + silence removal)
├── audio_transcription.py  # (To be added) Transcribe enhanced audio via AssemblyAI
├── API_secrets.py          # Store your AssemblyAI API key (confidential)
│
├── README.md
├── SETUP.md
└── requirements.txt
```

---

## 🧩 Installation Instructions

**1️⃣ Clone Repository**

```bash

git clone https://github.com/yourusername/audio-enhancement-transcription.git
cd audio-enhancement-transcription
```

**2️⃣  Install Python Dependencies**

```bash

pip install moviepy pydub librosa noisereduce pyAudioAnalysis soundfile scipy numpy requests
```

**3️⃣ Install FFmpeg**

FFmpeg is required for video-to-audio extraction:

- Windows
 Download from: https://ffmpeg.org/download.html
 Add FFmpeg to your system PATH.

- Linux (Ubuntu)
```bash
sudo apt update
sudo apt install ffmpeg
```

**4️⃣ Setup AssemblyAI API Key**

- Sign up at AssemblyAI
- Generate your API key.
- Create a file called API_secrets.py in the root folder:

  API_KEY_ASSEMBLYAI = 'your_assemblyai_api_key_here'

⚠️ Do not upload API_secrets.py publicly!

---

**🔄 Workflow: Full Process**


🔸 Step 1 — Video to Audio Conversion

Convert your video or non-WAV audio files into WAV format:

```bash

python "video to audio.py"
```

- You will be prompted to enter the file path:
- enter file path: input/your_video_or_audio_file.mp4
- Output will be saved as your_video_or_audio_file.wav in the same folder.
  

🔸 Step 2 — Audio Enhancement

Run noise reduction and silence removal:

```bash

python "AudioEnhancement (1).py"
```

You will be prompted to enter the file path:
- enter file path: input/your_converted_file.wav
- Enhanced output will be saved as enhanced_audio.wav in project directory.
- You may manually move this output into the enhanced/ folder for organization.
  

🔸 Step 3 — Audio Transcription (Speech-to-Text)

Note: The file audio_transcription.py will:

- Upload enhanced audio to AssemblyAI
- Poll transcription job status
- Retrieve and save text output into transcripts/ folder.

Example usage:

```bash
python audio_transcription.py enhanced/enhanced_audio.wav
```

---

**🎯 Sample End-to-End Flow**

```bash

python "video to audio.py"
python "AudioEnhancement (1).py"
python audio_transcription.py
```

**🔍 Troubleshooting**

- Make sure FFmpeg is correctly installed.
- Validate that your API_secrets.py file has correct AssemblyAI key.
- Check folder paths carefully (use absolute paths if necessary).
- If libraries fail to install, upgrade pip:

```bash

python -m pip install --upgrade pip
```

**🚀 Optional Improvements**

- Create automation scripts to fully automate the 3-step pipeline.
- Build a simple GUI using Tkinter or Streamlit.
- Extend transcription code to include speaker diarization and punctuation.




