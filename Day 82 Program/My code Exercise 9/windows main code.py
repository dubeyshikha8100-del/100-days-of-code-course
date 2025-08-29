
# FOR WINDOWS SOLUTION

import win32com.client

# Create a voice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Speak the text
persion = ["shivansh", "harry","shikha","disha","Rohan","hammad"]


for index,file in enumerate(persion):
    text = f" Shoutout to {persion[index]}"
    speaker.Speak(text)
    print(F"Shoutout to {persion[index]} Heart 💌")

