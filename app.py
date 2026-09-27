import streamlit as st
import subprocess
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Music Studio",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# PROFESSIONAL LIGHT THEME
# -------------------------------------------------

st.markdown("""
<style>

/* =================================
   MAIN PAGE
================================= */

.stApp {
    background: #f8fafc !important;
    color: #1e293b !important;
}

.block-container {
    max-width: 1200px;
    padding: 45px 55px 50px 55px;
}


/* =================================
   SIDEBAR
================================= */

section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb;
}

section[data-testid="stSidebar"] * {
    color: #263b55 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #172033 !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #718096 !important;
}

section[data-testid="stSidebar"] [data-testid="stAlert"] {
    background: #f1f7fc !important;
    border: 1px solid #dce8f2 !important;
}


/* =================================
   SIDEBAR OPEN / CLOSE ARROWS
================================= */

[data-testid="stSidebarCollapseButton"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}

[data-testid="stSidebarExpandButton"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}

[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarExpandButton"] button {
    color: #6f8499 !important;
    background: transparent !important;
    border: none !important;
}

[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarExpandButton"] svg {
    color: #6f8499 !important;
    fill: #6f8499 !important;
}

[data-testid="stSidebarCollapseButton"] button:hover,
[data-testid="stSidebarExpandButton"] button:hover {
    color: #48657f !important;
    background: #f1f5f9 !important;
}


/* =================================
   WELCOME AREA
================================= */

.welcome-small {
    color: #71839a !important;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 10px;
}

.main-heading {
    color: #172033 !important;
    font-size: 50px;
    font-weight: 750;
    line-height: 1.1;
    margin-bottom: 14px;
}

.description {
    color: #65758b !important;
    font-size: 18px;
    line-height: 1.7;
}


/* =================================
   CARDS
================================= */

.card {
    background: #ffffff !important;
    border: 1px solid #e3e9f0;
    border-radius: 20px;
    padding: 27px;
    margin-top: 24px;
    box-shadow: 0 5px 22px rgba(30, 41, 59, 0.05);
}

.card-title {
    color: #172033 !important;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 20px;
}


/* =================================
   SELECT BOXES
================================= */

div[data-baseweb="select"] > div {
    background: #ffffff !important;
    border: 1px solid #d9e2ec !important;
    border-radius: 10px !important;
    min-height: 48px;
    box-shadow: none !important;
}

div[data-baseweb="select"] * {
    color: #334155 !important;
}

div[data-baseweb="select"] svg {
    fill: #526b84 !important;
}


/* =================================
   SELECT LABELS
================================= */

.stSelectbox label {
    color: #52657a !important;
    font-weight: 600 !important;
}


/* =================================
   GENERATE BUTTON
================================= */

.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 12px;
    border: none !important;
    background: #7397bc !important;
    color: #ffffff !important;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 5px 12px rgba(85, 120, 155, 0.18);
}

.stButton > button:hover {
    background: #6288ad !important;
    color: #ffffff !important;
}


/* =================================
   AUDIO PLAYER
================================= */

audio {
    width: 100%;
    margin-top: 10px;
}


/* =================================
   METRICS
================================= */

[data-testid="stMetric"] {
    background: #f8fafc;
    border: 1px solid #e5eaf0;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
}

[data-testid="stMetricValue"] {
    color: #263b55 !important;
}


/* =================================
   DOWNLOAD BUTTONS
================================= */

.stDownloadButton > button {
    width: 100%;
    background: #ffffff !important;
    color: #31577d !important;
    border: 1px solid #bcd0e3 !important;
    border-radius: 12px !important;
    min-height: 50px;
    font-weight: 600;
}

.stDownloadButton > button:hover {
    background: #f1f7fc !important;
}


/* =================================
   ABOUT SECTION
================================= */

.about-box {
    background: #f1f8f7 !important;
    border: 1px solid #d8ebe7;
    border-radius: 18px;
    padding: 23px;
    margin-top: 28px;
}

.about-title {
    color: #24434a !important;
    font-size: 19px;
    font-weight: 700;
}

.about-text {
    color: #60747a !important;
    line-height: 1.7;
}


/* =================================
   FOOTER
================================= */

.footer {
    text-align: center;
    color: #94a3b8 !important;
    font-size: 13px;
    margin-top: 45px;
}


/* =================================
   HIDE ONLY UNNECESSARY STREAMLIT UI
================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/*
IMPORTANT:
Do NOT hide header.
Do NOT hide stToolbar.
They can contain the sidebar controls.
*/

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.markdown("## 🎵 AI Music Studio")

    st.caption("Turn your ideas into music")

    st.markdown("---")

    st.markdown("### 🏠 Home")
    st.markdown("### 🎶 My Music")
    st.markdown("### ℹ️ About")
    st.markdown("### ⚙️ Settings")

    st.markdown("---")

    st.info(
        "“Music is not just sound, "
        "it's a feeling.”"
    )


# -------------------------------------------------
# HERO
# -------------------------------------------------

st.markdown(
    '<div class="welcome-small">WELCOME TO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-heading">AI Music Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">'
    'Create unique music using artificial intelligence.<br>'
    'Choose your preferences and let the AI compose something special for you.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------------------------------------
# MUSIC SETTINGS
# -------------------------------------------------

st.markdown("""
<div class="card">

<div class="card-title">
🎵 Choose Your Music Style
</div>

</div>
""", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)


# -------------------------------------------------
# MOOD
# -------------------------------------------------

with col1:

    mood = st.selectbox(
        "🎭 Mood",
        [
            "Calm",
            "Happy",
            "Energetic",
            "Emotional",
            "Relaxing"
        ]
    )

selected_mood = mood


# -------------------------------------------------
# TEMPO
# -------------------------------------------------

with col2:

    tempo = st.selectbox(
        "⏱️ Tempo",
        [
            "Slow",
            "Medium",
            "Fast"
        ]
    )

selected_tempo = tempo


# -------------------------------------------------
# INSTRUMENT
# -------------------------------------------------

with col3:

    instrument = st.selectbox(
        "🎹 Instrument",
        [
            "Piano",
            "Acoustic Piano",
            "Electronic",
            "Ambient"
        ]
    )


# -------------------------------------------------
# DURATION
# -------------------------------------------------

with col4:

    duration = st.selectbox(
        "⏱️ Duration",
        [
            "30 Seconds",
            "1 Minute",
            "2 Minutes"
        ]
    )


# Convert selected duration into seconds

if duration == "30 Seconds":

    duration_seconds = 30

elif duration == "1 Minute":

    duration_seconds = 60

else:

    duration_seconds = 120


# -------------------------------------------------
# GENERATE BUTTON
# -------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)


if st.button(
    "✨  Generate Music  →",
    use_container_width=True
):

    st.session_state["generate_music"] = True


# -------------------------------------------------
# GENERATION
# -------------------------------------------------

if st.session_state.get("generate_music", False):

    with st.spinner("🎼 AI is composing your music..."):

        # -----------------------------------------
        # STEP 1 — Generate music
        # -----------------------------------------

        result = subprocess.run(
            ["python", "generate_music.py"],
            capture_output=True,
            text=True
        )


        if result.returncode != 0:

            st.error("Music generation failed.")

            st.code(result.stderr)


        else:

            # -----------------------------------------
            # STEP 2 — Create MIDI
            # -----------------------------------------

            midi_result = subprocess.run(
                ["python", "create_midi.py"],
                capture_output=True,
                text=True,
                env={
                    **os.environ,

                    "MUSIC_INSTRUMENT": instrument,

                    "MUSIC_DURATION": str(
                        duration_seconds
                    ),

                    "MUSIC_MOOD": selected_mood,

                    "MUSIC_TEMPO": selected_tempo
                }
            )


            if midi_result.returncode != 0:

                st.error("MIDI creation failed.")

                st.code(midi_result.stderr)


            else:

                # -----------------------------------------
                # STEP 3 — Convert MIDI to WAV
                # -----------------------------------------

                wav_result = subprocess.run(
                    ["python", "midi_to_wav.py"],
                    capture_output=True,
                    text=True
                )


                if wav_result.returncode != 0:

                    st.error("Audio conversion failed.")

                    st.code(wav_result.stderr)


                else:

                    st.success(
                        "🎉 Your music has been generated!"
                    )


                    # -----------------------------------------
                    # PLAYER
                    # -----------------------------------------

                    st.markdown("""
                    <div class="card">

                    <div class="card-title">
                    🎶 Your Generated Music
                    </div>

                    </div>
                    """, unsafe_allow_html=True)


                    if os.path.exists(
                        "generated_music.wav"
                    ):

                        with open(
                            "generated_music.wav",
                            "rb"
                        ) as f:

                            audio_data = f.read()


                        st.audio(
                            audio_data,
                            format="audio/wav"
                        )


                    # -----------------------------------------
                    # DETAILS
                    # -----------------------------------------

                    d1, d2, d3 = st.columns(3)


                    with d1:

                        st.metric(
                            "🤖 AI Model",
                            "LSTM"
                        )


                    with d2:

                        st.metric(
                            "🎹 Instrument",
                            instrument
                        )


                    with d3:

                        st.metric(
                            "⏱️ Tempo",
                            tempo
                        )


                    # -----------------------------------------
                    # DOWNLOADS
                    # -----------------------------------------

                    d1, d2 = st.columns(2)


                    if os.path.exists(
                        "generated_music.mid"
                    ):

                        with open(
                            "generated_music.mid",
                            "rb"
                        ) as f:

                            d1.download_button(
                                "⬇️ Download MIDI",
                                f,
                                file_name="AI_Generated_Music.mid",
                                mime="audio/midi",
                                use_container_width=True
                            )


                    if os.path.exists(
                        "generated_music.wav"
                    ):

                        with open(
                            "generated_music.wav",
                            "rb"
                        ) as f:

                            d2.download_button(
                                "⬇️ Download Audio",
                                f,
                                file_name="AI_Generated_Music.wav",
                                mime="audio/wav",
                                use_container_width=True
                            )


# -------------------------------------------------
# ABOUT
# -------------------------------------------------

st.markdown("""
<div class="about-box">

<div class="about-title">
💡 About This Project
</div>

<div class="about-text">

This application uses a trained LSTM neural network to
generate new sequences of musical notes based on patterns
learned from the training data.

</div>

</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("""
<div class="footer">

AI Music Studio &nbsp; • &nbsp;
Python &nbsp; • &nbsp;
TensorFlow &nbsp; • &nbsp;
LSTM &nbsp; • &nbsp;
Streamlit

</div>
""", unsafe_allow_html=True)