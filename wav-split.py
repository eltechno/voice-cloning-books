import os
import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_wav(file_name, min_silence_len=2000, silence_thresh=-30, chunk_length_ms=15000):
    audio = AudioSegment.from_wav(file_name)

    # split track where silence is 1 seconds or more and get chunks using 
    # the imported function.
    chunks = split_on_silence(audio, 
        # must be silent for at least 1 second
        min_silence_len=min_silence_len,

        # consider it silent if quieter than -16 dBFS
        silence_thresh=silence_thresh
    )

    # if any chunk is longer than 15 seconds, split it into 15-second chunks
    final_chunks = []
    for chunk in chunks:
        length_chunk_ms = len(chunk)
        if length_chunk_ms > chunk_length_ms:
            for i in range(0, length_chunk_ms, chunk_length_ms):
                final_chunks.append(chunk[i:i+chunk_length_ms])
        else:
            final_chunks.append(chunk)

    return final_chunks

def main():
    parser = argparse.ArgumentParser(description="Split a wav file into chunks")
    parser.add_argument("filepath", help="The filepath of the wav file to split")

    args = parser.parse_args()

    original_file_path = args.filepath
    original_file_name = os.path.basename(original_file_path)
    base_name = os.path.splitext(original_file_name)[0]

    # create a new directory for the chunks
    os.makedirs(base_name, exist_ok=True)

    chunks = split_wav(original_file_path)

    for i, chunk in enumerate(chunks):
        chunk.export(f"{base_name}/{base_name}-chunk{i}.wav", format="wav") # this will save chunks as "base_name/base_name-chunk0.wav", "base_name/base_name-chunk1.wav", etc.

if __name__ == "__main__":
    main()

