import openai
import json, os
import time as t

API_KEY = os.environ.get('OPEN_AI_KEY') #Enter your API key here
PREFIX = "emma_chapter_1"
MIMETYPE = ".mp3"
FILENAME = PREFIX + MIMETYPE

def main(filename):
    start = t.time()
    
    #Initialization
    openai.api_key = API_KEY
    print()
    print("Currently transcribing ", filename)

    #transcription call
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    json_object = json.dumps(transcript, indent=4)

    #write results
    transcrption_file = PREFIX + ".json"
    with open(transcrption_file, "w") as outfile:
        outfile.write(json_object)

    speed = t.time() - start

    print("Seconds to complete: ", speed)
    print("🥳 We did it! 🥳")


main(FILENAME)





