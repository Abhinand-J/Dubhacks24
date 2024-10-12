from flask import Flask
from flask import request
from flask import abort

app = Flask(__name__)
songs = [{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "song 1",
        "duration": "3:45",
        "artist": "bald nerd",
        "ytid": "paqcdLiBvsw",
    },{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "song 1",
        "duration": "3:45",
        "artist": "bald nerd",
        "ytid": "ZqY3eONjX54",
    },{
        "image": "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
        "name": "song 1",
        "duration": "3:45",
        "artist": "bald nerd",
        "ytid": "ZqY3eONjX5f",
    }]

@app.route("/")
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