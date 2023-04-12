import openai
import json, os
import time as t

API_KEY = os.environ.get('OPEN_AI_KEY')
PREFIX = "emma_chapter_9"
FILENAME = "../audios/" + PREFIX + ".mp3"

def main(filename):
    start = t.time()
    
    #Initialization
    openai.api_key = API_KEY
    print("Currently transcribing ", FILENAME)
    print()

    #transcription call
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    json_object = json.dumps(transcript, indent=4)

    #write results
    transcrption_file = './whisper_results/' + PREFIX + ".json"
    with open(transcrption_file, "w") as outfile:
        outfile.write(json_object)

    speed = t.time() - start

    print("Seconds to complete: ", speed)
    print("🥳 We did it! 🥳")


main(FILENAME)





