from pydub import AudioSegment

def split_mp3(file_name, chunk_length_ms=15000): # default chunk length is 15 seconds
    audio = AudioSegment.from_mp3(file_name)

    length_audio_ms = len(audio)
    chunks = []
    for i in range(0, length_audio_ms, chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        chunks.append(chunk)

    return chunks

def main():
    chunks = split_mp3("yourfile.mp3") # replace "yourfile.mp3" with your actual file path

    for i, chunk in enumerate(chunks):
        chunk.export(f"chunk{i}.mp3", format="mp3") # this will save chunks as "chunk0.mp3", "chunk1.mp3", etc.

if __name__ == "__main__":
    main()

