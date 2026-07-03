def transcribe_audio(model, audio_path, language=None):

    segments, info = model.transcribe(
        audio_path,
        language=language,
        task="transcribe",
        beam_size=5
    )

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip(), info.language