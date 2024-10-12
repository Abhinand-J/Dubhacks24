import Image from "next/image";
import Link from "next/link";

export default function SongPanel({ image, name, duration, artist, ytid }) {
    return (
        <div className="flex flex-col max-w-[300px]">
            <Link href={`/video/${ytid}`}>
                <Image
                    src={image}
                    className="rounded-2xl hover:rounded-none duration-300"
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
