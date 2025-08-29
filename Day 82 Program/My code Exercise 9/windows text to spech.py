import win32com.client
import random

# Create a voice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Original names
for  i in range(3):
    speaker.Speak()
