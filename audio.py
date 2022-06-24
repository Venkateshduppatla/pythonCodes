
import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('test.mp3') as source:
	#r.adjust_for_ambient_noise(source)
	print("Say Some Thing...")
	audio = r.listen(source)
	print("You Said: " + r.recognize_google(audio))
	input("")


# import azure.cognitiveservices.speech as speechsdk

# def azure_batch_stt(filename: str, lang: str, encoding: str) -> str:
#     speech_config = speechsdk.SpeechConfig(
#         subscription=AZURE_SPEECH_KEY,
#         region=AZURE_SERVICE_REGION
#     )
#     audio_input = speechsdk.AudioConfig(filename=filename)
#     speech_recognizer = speechsdk.SpeechRecognizer(
#         speech_config=speech_config,
#         audio_config=audio_input
#     )
#     result = speech_recognizer.recognize_once()

#     return result.text if result.reason == speechsdk.ResultReason.RecognizedSpeech else None

# TESTCASES = [
#   {
#     'filename': 'audio/2830-3980-0043.wav',
#     'text': 'experience proves this',
#     'encoding': 'LINEAR16',
#     'lang': 'en-US'
#   },
#   {
#     'filename': 'audio/4507-16021-0012.wav',
#     'text': 'why should one halt on the way',
#     'encoding': 'LINEAR16',
#     'lang': 'en-US'
#   },
#   {
#     'filename': 'audio/8455-210777-0068.wav',
#     'text': 'your power is sufficient i said',
#     'encoding': 'LINEAR16',
#     'lang': 'en-US'
#   }
# ]     

# for t in TESTCASES:
#     print('\naudio file="{0}"    expected text="{1}"'.format(
#         t['filename'], t['text']
#     ))
#     print('azure-batch-stt: "{}"'.format(
#         azure_batch_stt(t['filename'], t['lang'], t['encoding'])
#     ))

