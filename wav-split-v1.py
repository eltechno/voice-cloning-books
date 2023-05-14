import os
import argparse
from pydub import AudioSegment

def split_wav(file_name, chunk_length_ms=15000): # default chunk length is 15 seconds
    audio = AudioSegment.from_wav(file_name)

    length_audio_ms = len(audio)
    chunks = []
    for i in range(0, length_audio_ms, chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        chunks.append(chunk)

    return chunks

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

