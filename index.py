import boto3
import wikipedia
import os
from contextlib import closing
import sounddevice as sd
import sys


def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix


comprehend = boto3.client(service_name='comprehend')
polly = boto3.client(service_name='polly')
text = smart_truncate(wikipedia.summary("Seattle, Washington"))


response = polly.synthesize_speech(
    OutputFormat='mp3',
    SampleRate='22050',
    Text=text,
    TextType='text',
    VoiceId='Matthew'
)

if "AudioStream" in response:
    sd.play(response["AudioStream"], "22050")
        # try:
            
        #     # Open a file for writing the output as a binary stream
        #     # with open(output, "wb") as file:
        #     #     file.write(stream.read())
        # except :
        #     # Could not write to file, exit gracefully
        #     print("An err occurred")
        #     sys.exit(-1)

# playsound(os.path.join(os.getcwd(), "speech.mp3"))


# response = comprehend.detect_entities(
#         Text=,
#         LanguageCode='en'
# )


# pprint(response['Entities'])