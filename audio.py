import wave
import sys
import os
import pyaudio
import time
from google.cloud import speech
import pyphen

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "optimum-beach-438421-r2-cb7e5c25df48.json"
def recordUser(RECORD_SECONDS, folder_path, file_name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

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
    path = os.path.join(videoId, "clips.txt")
    with open(path, 'r') as file:
        for line in file:
            start, end = line.strip().split(" ")
            clips.append([start, end])
    return clips

def speechToText(file_path):
    client = speech.SpeechClient()
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        sample_rate_hertz=44100
    )
    response = client.recognize(config=config, audio=audio)
    ret = []
    for result in response.results:
        ret.append(result.alternatives[0].transcript)
    return ret
