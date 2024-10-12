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