# Whisper-Summarization
Repo containing the Whisper Summarization app as presented in Deepgrams Webinar: "Building Voice Products with Whisper API" (04/12/2023)

To run the code, follow these steps:

1. Create an environment variable containing your OpenAI API Key. The code assumes that this environment variable is named "OPEN_AI_KEY".

2. First run the transcribe_whisper.py file. The only variables you have to fill in are `PREFIX` (the title of the audio you wish to transcribe) and `MIMETYPE` (the type of audio file you have).

That is, if you have an audio named `emma_chapter_1.mp3`, the `PREFIX` should be set to `'emma_chapter_1'` and `MIMETYPE` should be set to `'.mp3'`. (Note the mimetype should be all-lowercase, and the '.' should be included.)

3. Run `transcribe_whisper.py` by calling `python3 transcribe_whisper.py`. After a few moments, a .json file should appear in your directory whose title matches the title of the audio you just transcribed. That is, if you transcribed an audio file called `phone_call.m4a`, the output transcription should be located in a file named `phone_call.json`.

4. To summarize the transcription, run `python3 summarize.py`. Note that the `PREFIX` variable in this file should match the `PREFIX` variable you used in the previous steps. (Or, to be more specific, the `PREFIX` variable here should be set to the title of the file that contains the transcription you wish to summarize).

5. The output of step 4 should be a .txt file containing the summary of the original audio. Again, the title of this .txt file should match the title of the .json that contains the original transcription.
