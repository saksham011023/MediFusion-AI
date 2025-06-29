# Setup Text to Speech-TTS model gTTS (Google Text to Speech)
import os
from gtts import gTTS
from dotenv import load_dotenv
import elevenlabs
from elevenlabs.client import ElevenLabs

load_dotenv()

def text_to_speech_old(input_text,output_path):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_path)

input_text="Hello, My name is Saksham! How you doing"
# text_to_speech_old(input_text=input_text,output_path="gtts_testing.mp3")
# Setup Text to Speech-TTS model ElevenLabs

def text_to_speech_with_elevenlabs_old(input_text: str, output_filepath: str, voice_name: str = "Lauren B - Romantic, Polished & Calm"):
    # 1. Initialize client
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    # 2. Find the voice ID for the given voice name
    voices = client.voices.search().voices
    matching = [v for v in voices if v.name == voice_name]
    if not matching:
        raise ValueError(f"Voice '{voice_name}' not found. Available voices: {[v.name for v in voices]}")
    voice_id = matching[0].voice_id

        # 3. Generate speech bytes
    audio_stream = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice_id,
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)


# text_to_speech_with_elevenlabs_old(input_text,output_filepath="elevenlabs_testing.mp3")

# Use model for text output to voice

import subprocess
import platform

def text_to_speech(input_text,output_path):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_path)

    os_name=platform.system()
    try:
        if os_name=="Darwin":  #macOS
            subprocess.run('afplay',output_path)
        elif os_name=="Windows":  #macOS
            subprocess.run([
                    "ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", output_path], check=True)

        elif os_name=="Linux":
            subprocess.run(['aplay',output_path])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}")

input_text="Hello, My name is Saksham! How you doing. New Version"
# text_to_speech(input_text=input_text,output_path="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text: str, output_filepath: str, voice_name: str = "Lauren B - Romantic, Polished & Calm"):
    # 1. Initialize client
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    # 2. Find the voice ID for the given voice name
    voices = client.voices.search().voices
    matching = [v for v in voices if v.name == voice_name]
    if not matching:
        raise ValueError(f"Voice '{voice_name}' not found. Available voices: {[v.name for v in voices]}")
    voice_id = matching[0].voice_id

        # 3. Generate speech bytes
    audio_stream = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice_id,
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    os_name=platform.system()
    try:
        if os_name=="Darwin":  #macOS
            subprocess.run('afplay',output_filepath)
        elif os_name=="Windows":  #macOS
            subprocess.run([
                    "ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", output_filepath], check=True)

        elif os_name=="Linux":
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}")


text_to_speech_with_elevenlabs(input_text,output_filepath="elevenlabs_testing_autoplay.mp3")