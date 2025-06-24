import librosa
import noisereduce as nr
from pyAudioAnalysis import audioSegmentation
import soundfile as sf
def enhance_audio(input_file, output_file):
    # Load the audio file
    audio, sr = librosa.load(input_file, sr=None)

    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=audio, sr=sr)

    # Perform background noise clearance
    segments = audioSegmentation.silence_removal(reduced_noise, sr, 0.05, 0.05, smooth_window=0.1)
    # Language identification
    segments_lang = []
    for seg in segments:
        segment_audio = reduced_noise[int(seg[0]*sr):int(seg[1]*sr)]
        segments_lang.append((seg, segment_audio))

    # Save the enhanced audio
    sf.write(output_file, reduced_noise, sr)

# Example usage
input_file = input("enter file path: ")
output_file = "enhanced_audio.wav"
enhance_audio(input_file, output_file)

