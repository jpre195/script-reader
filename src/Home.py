import wave

from piper import PiperVoice
import simpleaudio as sa
import streamlit as st


def main():

    st.set_page_config(layout = 'wide')
    st.title(body="Script Reader", anchor=False, text_alignment="center")

    cols = st.columns(2)

    with cols[0].container(border=True):
        st.header(body="Script", anchor=False, text_alignment="center")
        script = st.text_area(label="Script")

    with cols[1].container(border=True):
        st.header(body="Roles", anchor=False, text_alignment="center")

    go_btn = st.button(label="Go", key="go", type="primary")

    if go_btn:
        voice = PiperVoice.load('voices/en_US-amy-medium.onnx')

        with wave.open('wav_files/script.wav', 'wb') as wav_file:
            voice.synthesize_wav(script, wav_file)

        st.audio('wav_files/script.wav', autoplay = True)


if __name__ == "__main__":
    main()
