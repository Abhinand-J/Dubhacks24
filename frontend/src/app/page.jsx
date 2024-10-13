import SongPanel from "./components/song";

export default async function Home() {
    const resp = await fetch("http://localhost:5000/data")
    const songs = await resp.json()

    return (
        <div>
            <div>
                <div className="mb-8">
                    <h1 className="text-2xl font-bold">Welcome Back!</h1>
                </div>
                <div className="mb-12">
                    <form action="#" method="post" className="flex gap-8">
                        <input
                            type="text"
                            placeholder="Search Song"
                            className="rounded-full p-4 lg:min-w-[32rem] text-black"
                        />
                        <input type="submit" value="Submit" className="p-4 text-black duration-300 bg-white rounded-full hover:bg-slate-300"/>
                    </form>
                </div>
            </div>
            <div className="flex flex-wrap gap-8">
                {songs.map((song) => (
                    <SongPanel
                        image={`https://img.youtube.com/vi/${song.yt_id}/0.jpg`}
                        name={song.song_name}
                        artist={song.artist}
                        clip_id={song.clip_id}
                        key={song.clip_id}></SongPanel>
                ))}
            </div>
        </div>
    );
}
