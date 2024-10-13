"use client";

import { AudioRecorder } from "react-audio-voice-recorder";
import { useState } from "react";

const createWordSet = (inputString) => {
    const wordsArray = inputString.split(/\s+/);
    const wordSet = new Set(wordsArray);
    return wordSet;
}

export default function Audio(props) {
    const [grade, setGrade] = useState(0);
    const [you, setYou] = useState("")
    const [wordsToPractice, setWordsToPractice] = useState(new Set())

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
        formData.append("clip_id", props.clip_id);

        const response = await fetch("http://localhost:5000/submitMusicData", {
            method: "POST",
            body: formData,
        });

        const jaysone = await response.json();
        const og_set = createWordSet(jaysone[0])
        const new_set = createWordSet(jaysone[1])
        
        const difference = [...og_set].filter(word => !new_set.has(word));

        setYou(jaysone[1])
        setGrade(jaysone[3])
        setWordsToPractice(difference)

        
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
            <div id="audio-recording" className="m-auto">
                
            </div>
            <div>
                <p>{you != "" ? `We Heard: ${you}` : ""}</p>
                <p>{you != "" ? `Grade: ${Math.round(grade * 100)}%` : ""}</p>
                <p>{you != "" ? "Words to Practice: "+ Array.from(wordsToPractice).join(", ") : ""}</p>
            </div>
        </div>
    );
}
