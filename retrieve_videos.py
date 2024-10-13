# retrieve_videos.py
import json
from videos_data import videos  # Import video data from videos_data.py

# Function to retrieve all videos
def get_all_videos():
    return videos

# Function to retrieve a video by its ID
def get_video_by_id(video_id):
    for video in videos:
        if video['id'] == video_id:
            return video
    return None  # Return None if no video with the given ID is found
#name, artist, ytid
#lyrics=[[lyrics for clip1] [lyrics for clip2]]
#time-stamps = [[clip1start, clip1end], [clip2start, clip2end]]
def get_video(file_path):
    data = []
    clip_id = 0
    with open(file_path, "r") as f:
        lines = f.readlines()
        name = lines[0].strip()
        artist = lines[1].strip()
        ytid = lines[2].strip()
        curLine = 3
        while(curLine < len(lines)):
            numLine = int(lines[curLine].strip())
            curClip = {}
            curClip["song_name"] = name
            curClip["artist"] = artist
            curClip["yt_id"] = ytid
            curClip["lyrics"] = ""
            curClip["clip_id"] = ytid + "_" + str(clip_id)
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