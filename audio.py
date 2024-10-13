import datetime
import wave
import sys
import os
import pyaudio
import time
from google.cloud import speech
import pyphen
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "optimum-beach-438421-r2-0439c4342572.json"
def recordUser(RECORD_SECONDS, folder_path, file_name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    path = os.path.join(folder_path, file_name)

    with wave.open(path, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        #3 seconds countdown
        for i in range(3, 0, -1):
            print(f"{i} seconds left until recording start")
            time.sleep(1)
        
        print('Recording...')
        last_remaining_time = 6
        for _ in range(RATE // CHUNK * RECORD_SECONDS, -1, -1):
            wf.writeframes(stream.read(CHUNK))
            remaining_time = int((_*CHUNK+RATE-1)/RATE)
            if(remaining_time < last_remaining_time):
                print(f"{remaining_time} seconds left in recording")
                last_remaining_time = remaining_time

        print('Done')

        stream.close()
        p.terminate()
#fetch all clips from a video and return in list [start, end]
def fetchClips(videoId):
    clips = []
    path = os.path.join(videoId, "clips.txt") # Needs to be fixed
    with open(path, 'r') as file:
        for line in file:
            start, end = line.strip().split(" ")
            clips.append([start, end])
    return clips

def speechToText(file_path, language):
    client = speech.SpeechClient()
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code=language
    )
    response = client.recognize(config=config, audio=audio)

    return response.results

def parse_long_mp3(file_path):
    sound = AudioSegment.from_mp3(file_path)
    length_in_seconds = sound.duration_seconds
    split_count = int(length_in_seconds // 58 + 1)
    split_audio_filepaths = []
    total_lyrics = []

    if not os.path.exists(file_path[:-4]):
        os.makedirs(file_path[:-4])

    for i in range(split_count):
        sound[i * len(sound) // split_count:min((i + 1) * len(sound) // split_count, len(sound))].export(f"{file_path[:-4]}/{i}.mp3", format="mp3")
        split_audio_filepaths.append(f"{file_path[:-4]}/{i}.mp3")
    
    for i, filepath in enumerate(split_audio_filepaths):
        lyrics = speechToText(filepath)

        for j in range(len(lyrics)):
            lyrics[j].result_end_time += datetime.timedelta(seconds=i * 58)
        total_lyrics += lyrics

    return total_lyrics