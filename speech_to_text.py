#!PATH_TO_PYTHON3.6_INTERPRETER

import io
import json
import base64
import os

# Imports the Google Cloud client library
from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class SpeechText:
    _credentials = service_account.Credentials.from_service_account_file('ABSOLUTE_PATH_TO_GOOGLE_PRIVATE_KEY_JSON_FILE_ON_SERVER')
    _filePath = 'ABSOLUTE_PATH_ON_SERVER_TO_STORE_AUDIO_FILE'

    def __init__(self, file_name):
        self.file_name = file_name

    def getText(self):
        server_response = {}
        server_response['success'] = False
        try:            
            # Instantiates a client
            client = speech.SpeechClient(credentials=SpeechText._credentials)

            audio = None

            input_file = SpeechText._filePath + 'input.wav'
            ####create wav file from blob
            with io.open(input_file, 'wb') as write_file:
                write_file.write(base64.b64decode(self.file_name))

            # Loads the audio into memory
            with io.open(input_file, 'rb') as audio_file:
                content = audio_file.read()
                audio = types.RecognitionAudio(content=content)

            if audio is not None:
                ##### No need to give encoding and sample_rate_hertz for .wav and .flac files
                ##### For other file formats, you must provide encoding and sample_rate_hertz
                config = types.RecognitionConfig(
                #encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                language_code='en-US',
                # sample_rate_hertz=48000,
                )
                # Detects speech in the audio file
                response = client.recognize(config, audio)

                txt = ''
                for result in response.results:
                    txt += result.alternatives[0].transcript

                server_response['success'] = True
                server_response['txt'] = txt

        except Exception:
            server_response['msg'] = 'Exception occurred'

        return json.dumps(server_response)
