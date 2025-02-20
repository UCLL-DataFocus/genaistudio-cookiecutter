"""
speech.py

This module provides a SpeechRecognizer class to perform speech recognition using the SpeechRecognition library.
It supports capturing audio from a microphone or processing an audio file. Logging is used to trace execution and errors.
"""

import logging
import speech_recognition as sr

class SpeechRecognizer:
    """
    A class that encapsulates speech recognition functionalities using the SpeechRecognition library.
    
    Attributes:
        recognizer (sr.Recognizer): An instance of the Recognizer class.
        language (str): The language code for recognition (default is "en-US").
    """

    def __init__(self, language: str = "en-US"):
        """
        Initializes the SpeechRecognizer with the specified language.
        
        Args:
            language (str): The language code for recognition.
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
            str: The recognized text, or an empty string if recognition fails.
        """
        try:
            with sr.Microphone() as source:
                self.logger.info("Listening from microphone...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception as e:
            self.logger.error("Error accessing the microphone: %s", e)
            return ""

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            self.logger.info("Recognition successful: %s", text)
            return text
        except sr.RequestError as e:
            self.logger.error("API unavailable or unresponsive: %s", e)
        except sr.UnknownValueError:
            self.logger.error("Unable to recognize speech from the audio input.")
        return ""

    def recognize_from_file(self, file_path: str) -> str:
        """
        Perform speech recognition on an audio file.
        
        Args:
            file_path (str): The path to the audio file.
        
        Returns:
            str: The recognized text, or an empty string if recognition fails.
        """
        try:
            with sr.AudioFile(file_path) as source:
                self.logger.info("Reading audio file: %s", file_path)
                audio = self.recognizer.record(source)
        except Exception as e:
            self.logger.error("Error reading the audio file: %s", e)
            return ""

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            self.logger.info("File recognition successful: %s", text)
            return text
        except sr.RequestError as e:
            self.logger.error("API unavailable or unresponsive: %s", e)
        except sr.UnknownValueError:
            self.logger.error("Unable to recognize speech from the audio file.")
        return ""


if __name__ == "__main__":
    recognizer = SpeechRecognizer(language="en-US")
    
    print("Testing microphone input. Please speak into the microphone...")
    recognized_text = recognizer.recognize_from_microphone()
    print(f"Recognized Text: {recognized_text}")
