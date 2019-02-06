# python-simple-api-for-speech-to-text

Introduction: This is a simple API which converts audio to text using Google Speech library, sends information as the JSON response. It is build using Python language(Python3.6) and uses simple web(CGI) interface.

Pre-requisite:
 1. Google Account with private key json for details click https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
 2. Python3.6
 3. google-cloud-speech installed into the server.
 
Usage: Capture User voice using microphone and send the audio in the form of blob file to the **get-speech-text.py** file which then calls **speech_to_text** to convert audio into text. The audio file must be a blob file genearted using any of js liberaries like https://subinsb.com/html5-record-mic-voice/.

Note: get-speech-text.py and speech-text.py are very basic files. It only supports English language audio and text. Please edit the files for further customizations. For list of languages, audio format, encoding, sample rate and other features please visit supported by Google Speech liberary please visit https://cloud.google.com/speech-to-text/docs/
