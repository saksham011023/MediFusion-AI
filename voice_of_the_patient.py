#Setup Audio Recoder (ffmpeg and PyAudio)
import os
import logging
import speech_recognition as sr
import pydub
from pydub import AudioSegment
from io import BytesIO
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path,timeout=20,phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an mp3 file.

    Args:
    file_path (str): Path to save the recorded audio fil.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_limit (int) : Maximum time for the phrase to record (in seconds).
    """
    recognizer=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise....")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            logging.info("Start Speaking now....")

            # Record the Audio
            audio_data=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("Recording Complete.")

            #Convert the recorded audio to mp3 file
            wav_data=audio_data.get_wav_data()
            audio_segment=AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path,format="mp3",bitrate="128k")

            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occured: {e}")

audio_file_path="patient_voice_test.mp3"
# record_audio(file_path=audio_file_path)

# Setup Speech to text-STT-model for transcription

# 
# stt_model="whisper-large-v3"  #speech to text model
def transcribe_with_groq(stt_model,audio_filepath,GROQ_API_KEY):
    client=Groq(api_key=os.getenv("GROQ_API_KEY"))

    audio_file=open(audio_file_path,"rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text
