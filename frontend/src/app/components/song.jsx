import Image from "next/image";
import Link from "next/link";

export default function SongPanel({ image, name, duration, artist, clip_id }) {
    return (
        <div className="flex flex-col max-w-[300px]">
            <Link href={`/video/${ytid}`}>
                <Image
                    src={image}
                    className="duration-300 rounded-2xl hover:rounded-none"
                    width={300}
                    height={250}
                />
                <div>
                    <div className="flex justify-between w-full my-1">
                        <p className="font-bold">{name}</p>
                        <p>{duration}</p>
                    </div>
                    <div>
                        <p>{artist}</p>
                    </div>
                </div>
            </Link>
        </div>
    );
}
