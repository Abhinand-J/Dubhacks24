"use client";

import { AudioRecorder } from "react-audio-voice-recorder";

export default async function Audio(props) {
    const addAudioElement = (blob) => {
        const url = URL.createObjectURL(blob);
        const audio = document.createElement("audio");
        audio.src = url;
        audio.controls = true;

        submitData(blob);

        const target = document.getElementById("audio-recording");
        target.innerHTML = "";
        target.appendChild(audio);
    };

    const submitData = async (data) => {
        const formData = new FormData();
        formData.append("file", data, "temp.mp3");
        formData.append('clip_id', props.clip_id);

        
        let response = await fetch("http://localhost:5000/submitMusicData", {
            method: "POST",
            body: formData
        });
    };

    return (
        <div className="flex flex-col gap-4">
            <div className="m-auto">
                <AudioRecorder
                    onRecordingComplete={addAudioElement}
                    audioTrackConstraints={{
                        noiseSuppression: true,
                        echoCancellation: true,
                    }}
                    downloadOnSavePress={false}
                    downloadFileExtension="webm"
                    className="m-auto"
                />
            </div>
            <div id="audio-recording" className="m-auto"></div>
        </div>
    );
}
