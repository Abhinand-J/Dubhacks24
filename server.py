from flask import Flask
from flask import request
from flask import abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
songs = [{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "Into the Unknown",
        "duration": "3:30",
        "artist": "Idina Menzel",
        "ytid": "gIOyB9ZXn8s",
    },{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "Love Story",
        "duration": "3:56",
        "artist": "Taylor Swift",
        "ytid": "8xg3vE8Ie_E",
    },{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "song 1",
        "duration": "3:45",
        "artist": "bald nerd",
        "ytid": "ZqY3eONjX5f",
    }]

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