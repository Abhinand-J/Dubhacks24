"use client";

import { useRouter } from "next/navigation";
import { AudioRecorder } from "react-audio-voice-recorder";

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
    let response = await fetch("http://localhost:5000/sendMusicData", {
        method: "POST",
        body: JSON.stringify({
            data: data
        }),
        headers: {
            "Content-type": "application/json",
        },
    });
};

export default function Page({ params }) {
    const router = useRouter();
    return (
        <div className="flex flex-col justify-center max-w-full gap-6 align-middle">
            <iframe
                className="w-full m-auto aspect-video"
                src={`https://www.youtube.com/embed/${params.yt_id}`}
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
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
