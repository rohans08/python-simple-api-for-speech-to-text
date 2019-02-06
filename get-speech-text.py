#!PATH_TO_PYTHON3.6_INTERPRETER

import cgi
from speech_to_text import SpeechText
import re

print("Content-Type: application/json\r\n")


form = cgi.FieldStorage()
file_name = form.getvalue('filename')

#### if blob file has first 22 lines as data:audio/wav;base64, then remove them
#### else coment out the lines below
if file_name is not None:
    file_name = re.sub(r'data:audio/wav;base64,', '', file_name)

speechToTextObj = SpeechText(file_name)
responseText    = speechToTextObj.getText()
print(responseText)
