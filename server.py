from flask import Flask
from flask import request
from flask import abort
from flask_cors import CORS
import os
from grader import grader
from retrieve_videos import get_video
import json
from pydub import AudioSegment

app = Flask(__name__)
CORS(app)

with open("data.json", "r") as file:
    songs = json.load(file)

# script_dir = os.path.dirname(__file__)
# rel_path = "videos"
# directory_path = os.path.join(script_dir, rel_path)

# for file in os.listdir(directory_path):
#     if file.endswith(".txt"):
#         songs.append(get_video(os.path.join(directory_path, file)))


@app.route("/data")
def hello_world():
    return songs

@app.route("/fetch")
def fetch_song():
    clip_id = request.args.get('clip_id')

    if clip_id == "":
        abort(404)

    for song in songs:
        if song["clip_id"] == clip_id:
            return song
    
    abort(403)

@app.route("/submitMusicData", methods=["POST"])
def print_song():
    files = request.files
    clip_id = request.form["clip_id"]
    file_storage = files.get('file')
    file_storage.save(f"mp3/{clip_id}.webm")

    audio = AudioSegment.from_file(f"mp3/{clip_id}.webm")
    audio.export(f"mp3/{clip_id}.wav", format="wav")

    graded_score = grader(clip_id)

    return json.dumps(graded_score)

