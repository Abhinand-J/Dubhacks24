# retrieve_videos.py
import json

def get_video(file_path):
    data = []
    clip_id = 0
    with open(file_path, "r") as f:
        lines = f.readlines()
        name = lines[1].strip()
        artist = lines[2].strip()
        ytid = lines[3].strip()
        language = lines[0].strip()
        curLine = 4
        while(curLine < len(lines)):
            numLine = int(lines[curLine].strip())
            curClip = {}
            curClip
            curClip["song_name"] = name
            curClip["artist"] = artist
            curClip["yt_id"] = ytid
            curClip["lyrics"] = ""
            curClip["clip_id"] = ytid + "_" + str(clip_id)
            curClip["language"] = language
            clip_id += 1
            for i in range(numLine):
                curLine+=1
                curClip["lyrics"] += (lines[curLine].strip())
                curClip["lyrics"] += " "
            curLine += 1
            start, end = lines[curLine].strip().split(" ")
            curClip["start"] = start
            curClip["end"] = end
            curLine += 1
            data.append(curClip)
    return data

with open("data.json", "w") as f:
    data = get_video("videos/love-story.txt")
    json.dump(data, f)