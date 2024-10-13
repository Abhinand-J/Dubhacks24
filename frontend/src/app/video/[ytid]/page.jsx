import Audio from "@/app/components/AudioRecorder";

export default async function Page({ params }) {
    const resp = await fetch(
        `http://localhost:5000/fetch?clip_id=${params.ytid}`
    );
    const song_data = await resp.json();

    return (
        <div className="flex flex-col justify-center max-w-full gap-6 align-middle">
            <div>
                <h1 className="text-4xl font-bold text-center">
                    {song_data.song_name + " " + 
                        song_data.clip_id.split("_")[
                            song_data.clip_id.split("_").length - 1
                        ]}
                </h1>
            </div>
            <iframe
                className="w-full lg:max-w-[60%] m-auto aspect-video"
                src={`https://www.youtube.com/embed/${song_data.yt_id}?start=${song_data.start}&end=${parseInt(song_data.end) + 1}`}
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
            <p className="text-center">{song_data.lyrics}</p>
            <Audio clip_id={song_data.clip_id} />
        </div>
    );
}
