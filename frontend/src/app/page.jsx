import SongPanel from "./components/song";

export default function Home() {
    const songs = [
        {
            image: "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
            name: "song 1",
            duration: "3:45",
            artist: "bald nerd",
            ytid: "paqcdLiBvsw",
        },
        {
            image: "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
            name: "song 1",
            duration: "3:45",
            artist: "bald nerd",
            ytid: "ZqY3eONjX54",
        },
        {
            image: "https://ged.com/wp-content/uploads/resized/2023/10/Online-GED-Test-Illustration_Copy_2-3x-768x0-c-default.png",
            name: "song 1",
            duration: "3:45",
            artist: "bald nerd",
            ytid: "ZqY3eONjX5f",
        },
    ];

    return (
        <div>
            <div>
                <div className="mb-8">
                    <h1 className="font-bold text-2xl">Welcome Back!</h1>
                </div>
                <div className="mb-12">
                    <form action="#" method="post" className="gap-8 flex">
                        <input
                            type="text"
                            placeholder="Search Song"
                            className="rounded-full p-4 lg:min-w-[32rem]"
                        />
                        <input type="submit" value="Submit" className="rounded-full p-4 bg-white text-black hover:bg-slate-300 duration-300"/>
                    </form>
                </div>
            </div>
            <div className="flex flex-wrap gap-8">
                {songs.map((song) => (
                    <SongPanel
                        image={song.image}
                        name={song.name}
                        duration={song.duration}
                        artist={song.artist}
                        ytid={song.ytid}
                        key={song.ytid}></SongPanel>
                ))}
            </div>
        </div>
    );
}
