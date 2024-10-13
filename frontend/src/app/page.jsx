import SongPanel from "./components/song";

export default function Home() {
    const songs = fetch("http://localhost:5000/")

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
                            className="rounded-full p-4 lg:min-w-[32rem]"
                        />
                        <input type="submit" value="Submit" className="p-4 text-black duration-300 bg-white rounded-full hover:bg-slate-300"/>
                    </form>
                </div>
            </div>
            <div className="flex flex-wrap gap-8">
                {songs.map((song) => (
                    <SongPanel
                        image={`https://img.youtube.com/vi/${song.yt_id}/0.jpg`}
                        name={song.name}
                        artist={song.artist}
                        yt_id={song.yt_id}
                        key={song.clip_id}></SongPanel>
                ))}
            </div>
        </div>
    );
}
