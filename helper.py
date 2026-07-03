import os

def save_audio(audio_bytes):
    os.makedirs("audio", exist_ok=True)

    audio_path = "audio/sample.wav"

    with open(audio_path, "wb") as f:
        f.write(audio_bytes)

    return audio_path