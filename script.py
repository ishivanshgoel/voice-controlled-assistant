# @author1 ishivanshgoel
# @author2 Pratyush1211

import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import serial
import pyjokes

## env varaibles
TEAMS_PATH = os.environ.get('TEAMS_PATH')
SERIAL_PORT = os.environ.get('SERIAL_PORT')
SERIAL_PORT_NUMBER = os.environ.get('SERIAL_PORT_NUMBER')
SERIES_DIRECTORY = os.environ.get('SERIES_DIRECTORY')

# voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# # set serial port for browser
ser = serial.Serial(SERIAL_PORT, SERIAL_PORT_NUMBER)

# # setting default browser
browser = webbrowser.get('windows-default')

# pass string to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# to greet the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    name =("Everyone")
    speak("Please tell me how may I help you")
    speak(name)

# to read voice command from mobile application
def takeCommand():
    while True:
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        if(len(data)>0):
            speak('Your command is '+data)
            return data
    return "the time"


if __name__ == "__main__":
    wishMe()
    while True:
        
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)

        if(len(data)>0):

            query = str(data).lower()
            print(query)
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                print('Query ', query)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            # open youtube
            elif 'open youtube' in query:
                browser.open('https://www.youtube.com')

            # open google
            elif 'open google' in query:
                browser.open('https://www.google.com')

            # open ms teams
            elif 'open teams' in query:
                os.system(TEAMS_PATH)
            
            elif 'tell jokes' in query:
                speak(pyjokes.get_joke())

            # open ms teams
            elif 'play series' in query:
                music_dir = SERIES_DIRECTORY
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            if(len(query)>0):
                break