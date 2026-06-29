from pathlib import Path

import ffmpeg


class AudioPipeline:

    SAMPLE_RATE = 16000
    CHANNELS = 1

    @staticmethod
    def convert_to_wav(
        input_file: str,
    ) -> str:

        input_path = Path(input_file)

        processing_dir = input_path.parent / "processing"

        processing_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = (
            processing_dir /
            f"{input_path.stem}.wav"
        )

        try:

            print("=" * 60)
            print("Input Path :", input_path.resolve())
            print("Input Exists :", input_path.exists())
            print("Output Path :", output_path.resolve())
            print("=" * 60)

            (
                ffmpeg
                .input(str(input_path))
                .output(
                    str(output_path),
                    acodec="pcm_s16le",
                    ac=AudioPipeline.CHANNELS,
                    ar=AudioPipeline.SAMPLE_RATE,
                )
                .overwrite_output()
                .run(
                    capture_stdout=True,
                    capture_stderr=True,
                )
            )

        except ffmpeg.Error as e:

            raise RuntimeError(
                e.stderr.decode()
            )

        return str(output_path)