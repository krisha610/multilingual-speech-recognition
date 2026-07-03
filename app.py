import streamlit as st
from audio_recorder_streamlit import audio_recorder

from models.whisper_model import load_model
from utils.transcriber import transcribe_audio
from utils.helper import save_audio

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="AI Multilingual Speech Recognition",
    page_icon="🎤",
    layout="centered"
)

# ------------------------------------------------
# Load Model Once (IMPORTANT FOR SPEED)
# ------------------------------------------------
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# ------------------------------------------------
# Custom CSS
# ------------------------------------------------
st.markdown("""
<style>

.block-container{
    padding-top: 2rem;
}

.stButton > button{
    width:100%;
    background: linear-gradient(90deg,#6C63FF,#9D4EDD);
    color:white;
    border:none;
    border-radius:15px;
    height:55px;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    color:white;
}

.language-box{
    background:#F4F1FF;
    padding:15px;
    border-radius:15px;
    border-left:6px solid #6C63FF;
}

.transcript-box{
    background:#F8F9FA;
    padding:25px;
    border-radius:15px;
    border-left:8px solid #6C63FF;
    font-size:18px;
    line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Sidebar
# ------------------------------------------------
with st.sidebar:
    st.title("📌 Project Details")

    st.write("### 🌍 Supported Languages")
    st.write("🇬🇧 English")
    st.write("🇮🇳 Hindi")
    st.write("🇮🇳 Gujarati")
    st.write("🇮🇳 Marathi")

    st.markdown("---")

    st.write("### 🛠 Tech Stack")
    st.write("• Streamlit")
    st.write("• Faster Whisper")
    st.write("• PyTorch")
    st.write("• Audio Recorder")

# ------------------------------------------------
# Gradient Header
# ------------------------------------------------
st.markdown("""
<div style="
background: linear-gradient(90deg,#6C63FF,#9D4EDD,#FF4D6D);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:30px;
box-shadow:0 8px 20px rgba(0,0,0,0.15);
">
<h1 style="margin:0;">🎤 AI Multilingual Speech Recognition</h1>
<p style="font-size:18px;margin-top:10px;">
English • Hindi • Gujarati • Marathi
</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Language Selection
# ------------------------------------------------
st.markdown("### 🌍 Select Language")

language_option = st.selectbox(
    "",
    [
        "Auto Detect",
        "English",
        "Hindi",
        "Gujarati",
        "Marathi"
    ]
)

language_map = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Marathi": "mr"
}

selected_language = None

if language_option != "Auto Detect":
    selected_language = language_map[language_option]

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------
# Recording Card
# ------------------------------------------------
st.markdown("""
<div style="
background:#F4F7FF;
padding:20px;
border-radius:20px;
border:2px solid #E0E7FF;
margin-bottom:20px;
">
<h3>🎙️ Record Your Voice</h3>
<p>Click the microphone below and start speaking.</p>
</div>
""", unsafe_allow_html=True)

audio_bytes = audio_recorder(
    text="",
    recording_color="#FF4B4B",
    neutral_color="#6C63FF",
    icon_name="microphone",
    icon_size="3x"
)

# ------------------------------------------------
# Audio Preview
# ------------------------------------------------
if audio_bytes:

    st.success("✅ Audio Recorded Successfully")

    st.audio(audio_bytes, format="audio/wav")

    if st.button("🚀 Start Transcription"):

        with st.spinner("🧠 Processing your speech..."):

            audio_path = save_audio(audio_bytes)

            transcript, detected_language = transcribe_audio(
                model,
                audio_path,
                selected_language
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="language-box">
             <b>Detected Language:</b> {detected_language.upper()}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("## 📝 Transcript")

        st.markdown(
            f"""
            <div class="transcript-box">
            {transcript}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            "📥 Download Transcript",
            transcript,
            file_name="transcript.txt"
        )

st.markdown("---")
st.caption(
    "Built with using Streamlit + Faster Whisper + PyTorch"
)