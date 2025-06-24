import os
import moviepy.editor as mp
from pydub import AudioSegment

def convert_to_wav(file_path):
    # Checking if the file is a video file
    video_extensions = ['.mp4','.avi','.mov','.webm','.mkv']  # can add more video extensions if needed
    audio_extensions = ['.mp3', '.wav', '.opus']  # can Add more audio extensions if needed

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in video_extensions:
        # Loading the video file
        video = mp.VideoFileClip(file_path)

        # Extracting audio from the video
        audio = video.audio

        # Constructing the output file path with .wav extension
        wav_file_path = os.path.splitext(file_path)[0] + '.wav'

        # Using ffmpeg to convert the video audio to WAV format
        audio.write_audiofile(wav_file_path, codec='pcm_s16le', bitrate='16k')

        print(f'Video file converted to WAV format: {wav_file_path}')
    elif file_extension in audio_extensions:
        # Loading the audio file
        audio = AudioSegment.from_file(file_path)

        # Converting audio to WAV format if not already in WAV
        if audio.frame_rate != 44100 or audio.channels != 1:
            audio = audio.set_frame_rate(44100).set_channels(1)
            wav_file_path = os.path.splitext(file_path)[0] + '.wav'
            audio.export(wav_file_path, format='wav')
            print(f'Audio file converted to WAV format: {wav_file_path}')
        else:
            print('Audio file is already in WAV format')
    else:
        print('Invalid file format')

# calling the function
file_path = input("enter file path: ") 
convert_to_wav(file_path)