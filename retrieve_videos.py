# retrieve_videos.py

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
    curVideo = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        curVideo["name"] = lines[0].strip()
        curVideo["artist"] = lines[1].strip()
        curVideo["ytid"] = lines[2].strip()
        curVideo["time-stamps"] = []
        curVideo["lyrics"] = []
        curLine = 3
        while(curLine < len(lines)):
            numLine = int(lines[curLine].strip())
            curLyrics = []
            for i in range(numLine):
                curLine+=1
                curLyrics.append(lines[curLine].strip())
            curVideo["lyrics"].append(curLyrics)
            curLine += 1
            start, end = lines[curLine].strip().split(" ")
            curVideo["time-stamps"].append([int(start), int(end)])
            curLine += 1
    return curVideo
