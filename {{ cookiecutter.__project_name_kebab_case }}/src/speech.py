"""
speech.py

Provides a SpeechRecognizer class to handle speech recognition.
Supports both microphone input and audio file processing.
Automatically adapts to Streamlit UI if available.
"""

import logging
import speech_recognition as sr

try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False


class SpeechRecognitionError(Exception):
    """Custom exception for speech recognition errors."""
    pass


class SpeechRecognizer:
    """
    Encapsulates speech recognition using the SpeechRecognition library.

    Attributes:
        recognizer (sr.Recognizer): Speech recognition engine.
        language (str): Language for speech recognition (default: "nl").
    """

    def __init__(self, language: str = "nl"):
        """
        Initializes the SpeechRecognizer.

        Args:
            language (str): Language code for recognition.
        """
        self.recognizer = sr.Recognizer()
        self.language = language

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info("SpeechRecognizer initialized with language: %s", self.language)

    def recognize_from_microphone(self, timeout: int = 5, phrase_time_limit: int = 10) -> str:
        """
        Capture audio from the microphone and convert it to text.

        Args:
            timeout (int): Maximum seconds to wait for phrase start.
            phrase_time_limit (int): Maximum seconds to capture after phrase detection.

        Returns:
            str: The recognized text.
        
        Raises:
            SpeechRecognitionError: If recognition fails.
        """
        try:
            with sr.Microphone() as source:
                self.logger.info("Listening from microphone...")
                st.info("🎤 Speak into the microphone...") if HAS_STREAMLIT else print("🎤 Speak into the microphone...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception as e:
            raise SpeechRecognitionError(f"Error accessing the microphone: {e}")

        return self._recognize_audio(audio)

    def recognize_from_file(self, audio_path: str) -> str:
        """
        Process an audio file and recognize speech.

        Args:
            audio_path (str): Path to the audio file.

        Returns:
            str: The recognized text.

        Raises:
            SpeechRecognitionError: If file processing fails.
        """
        try:
            with sr.AudioFile(audio_path) as source:
                self.logger.info(f"Processing audio file: {audio_path}")
                audio = self.recognizer.record(source)
        except Exception as e:
            raise SpeechRecognitionError(f"Error processing audio file: {e}")

        return self._recognize_audio(audio)

    def _recognize_audio(self, audio) -> str:
        """
        Helper method to recognize speech from audio.

        Args:
            audio (sr.AudioData): The recorded audio data.

        Returns:
            str: Recognized text.

        Raises:
            SpeechRecognitionError: If recognition fails.
        """
        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            self.logger.info("Recognition successful: %s", text)
            return text
        except sr.RequestError as e:
            raise SpeechRecognitionError(f"API unavailable or unresponsive: {e}")
        except sr.UnknownValueError:
            raise SpeechRecognitionError("Unable to recognize speech from the audio input.")


def get_speech_input(language="nl"):
    """
    Provides a flexible interface for getting speech input.

    If Streamlit is available, it uses an interactive UI.
    Otherwise, it defaults to CLI microphone input.

    Returns:
        str: Recognized speech text.
    """
    recognizer = SpeechRecognizer(language)

    if HAS_STREAMLIT:
        st.title("🗣️ Speech Recognition")
        st.write("Click below to start recording.")

        if st.button("🎙️ Start Recording"):
            try:
                text = recognizer.recognize_from_microphone()
                st.success(f"Recognized Text: {text}")
                return text
            except SpeechRecognitionError as e:
                st.error(f"❌ {e}")
                return ""

    else:
        print("🎙️ Press ENTER to start recording...")
        input()  # Wait for user to press enter
        try:
            text = recognizer.recognize_from_microphone()
            print(f"✅ Recognized Text: {text}")
            return text
        except SpeechRecognitionError as e:
            print(f"❌ {e}")
            return ""


if __name__ == "__main__":
    get_speech_input("nl")
