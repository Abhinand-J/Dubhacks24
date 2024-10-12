import wave
import sys
import os
import pyaudio
import time


def recordUser(RECORD_SECONDS, folder_path, file_name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = 5

    path = os.path.join(folder_path, file_name)

    with wave.open(path, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        # 3 seconds countdown
        for i in range(3, 0, -1):
            print(f"{i} seconds left until recording start")
            time.sleep(1)

        print('Recording...')
        last_remaining_time = 6
        for _ in range(RATE // CHUNK * RECORD_SECONDS, -1, -1):
            wf.writeframes(stream.read(CHUNK))
            remaining_time = int((_ * CHUNK + RATE - 1) / RATE)
            if (remaining_time < last_remaining_time):
                print(f"{remaining_time} seconds left in recording")
                last_remaining_time = remaining_time

        print('Done')

        stream.close()
        p.terminate()


# fetch all clips from a video and return in list [start, end]
def fetchClips(videoId):
    clips = []
    path = os.path.join(videoId, "clips.txt")
    with open(path, 'r') as file:
        for line in file:
            start, end = line.strip().split(" ")
            clips.append([start, end])
    return clips


# recordUser(5, "videoId", "clip1.wav")
videoid = "NlsHKnGuRg"
clips = fetchClips(videoid)
print(clips)