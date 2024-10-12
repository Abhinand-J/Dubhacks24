"use client";

import { useRouter } from "next/navigation";
import { AudioRecorder } from "react-audio-voice-recorder";

const addAudioElement = (blob) => {
    const url = URL.createObjectURL(blob);
    const audio = document.createElement("audio");
    audio.src = url;
    audio.controls = true;

    const target = document.getElementById("audio-recording");
    target.innerHTML = "";
    target.appendChild(audio);
};

export default function Page({ params }) {
    const router = useRouter();
    return (
        <div className="flex flex-col justify-center align-middle max-w-full gap-6">
            <iframe
                className="m-auto w-full aspect-video"
                src={`https://www.youtube.com/embed/${params.ytid}`}
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
