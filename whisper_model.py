from faster_whisper import WhisperModel

def load_model():
    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8"
    )
    return model