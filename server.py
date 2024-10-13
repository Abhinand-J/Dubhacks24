from flask import Flask
from flask import request
from flask import abort
from flask_cors import CORS, cross_origin
import os
from retrieve_videos import get_video

app = Flask(__name__)
cors = CORS(app)


songs = []

script_dir = os.path.dirname(__file__)
rel_path = "videos"
directory_path = os.path.join(script_dir, rel_path)

for file in os.listdir(directory_path):
    if file.endswith(".txt"):
        songs.append(get_video(os.path.join(directory_path, file)))


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fetch")
def fetch_song():
    ytid = request.args.get('username')

    if ytid == "":
        abort(404)

    for song in songs:
        if song.ytid == ytid:
            return song
        
@app.route("/sendMusicData", methods=["POST"])
@cross_origin()
def print_song():
    print(request)
    return "hi"

