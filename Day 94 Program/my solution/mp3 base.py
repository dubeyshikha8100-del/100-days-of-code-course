
# VeXERCISE SOLUTION FILE
# This file contains the solution to the exercise in the VeXERCISE.

# IMPORTING WIN32.CLIENT TO TEXT TO SPECH FUNCTIONALITY
import win32com.client as wincl

# IMPORT8ING DATETIME MODULE TO USE TIME FUNCTIONALITY
import datetime

# CREATE A WINDOWS TO TEXT TO SPEECH OBJECT
speak = wincl.Dispatch("SAPI.SpVoice")

#CRAETE A TRIME OBJECT
time = datetime.datetime.now().strftime("%I:%M %p")

# create a function to speak ton drink water time and sleep 40 minutes 40 minutes ago it will speak again
def water():
    global time # use the global time variable
    speak.Speak("It's time to drink water")
    speak.Speak("The time is " + time)
    done = input("Type 'done' after drinking water: ")
    if done.lower() == 'done':
        speak.Speak("Good job! Stay hydrated.")
    else:
        speak.Speak("Please type 'done' after drinking water.")
    log = open("water_log.txt", "a")
    log.write(f"Drank water at {time}\n")  
    log.close()   

    # sleep for 40 minutes
    import time
    time.sleep(2400)

#function run the while loop to run the water function every 40 minutes
def main():
    while True:
        speak.speak("Hello, I am your health assistant.")
        water()

if __name__ == "__main__":
    main()  