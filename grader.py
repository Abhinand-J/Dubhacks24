from audio import speechToText
import json
from compare_lyrics import edit_dist_dp
import os

print("HELLO THERE IS SOMETHING GOING ON HERRE")

# takes input of where clip is, and the language it's recorded in
def grader(clipID, lang):

    currentDir = os.path.dirname(__file__)
    folderPath = os.path.join(currentDir, 'mp3') # name of folder

    clipLocation = ""

    for file in os.listdir(folderPath):
        if file == ("" + clipID + ".wav"):
            clipLocation = os.path.join(folderPath, file)
    print(clipLocation)
    userLyrics = speechToText(clipLocation, lang) # stores calculated text

    file_path = "data.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    songLyrics = ""
    for clip in data:
        if clip['clip_id'] == clipID:
            songLyrics = clip['lyrics']
    if(songLyrics==""):
        raise Exception("bruh")
    incorrectChars, invertScore = edit_dist_dp(songLyrics, userLyrics)


    score = 1 - invertScore/(len(songLyrics) + len(userLyrics))

    print(score)

    return songLyrics, incorrectChars, score


correctLyrics, mistakes, score = grader("8xg3vE8Ie_E_0", "en-US")