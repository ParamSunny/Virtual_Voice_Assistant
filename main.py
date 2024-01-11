
import pyautogui
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import sys
import os
import openai
import datetime
import psutil

pyautogui.press('enter')

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def take1Command():
    r = sr.Recognizer()
    with sr.Microphone() as source1:
        r.pause_threshold = 0.5
        audio1 = r.listen(source1)
        try:
            print("Recognizing")
            firstquery = r.recognize_google(audio1, language="en-in")
            print(f"User said: {firstquery}")
            return firstquery
        except Exception as e:
            return " sorry, you are not my boss"



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return " sorry sir I can't understand what you want to say"


if __name__ == "__main__":

    st = "true"
    stt = "true"
    count = 0


    say("Hello, I am Friday")
    while stt == "true":
        print("Listening...")
        firstquery = take1Command()
        if firstquery.lower() == "hello friday":
            say("Oooo hello sir, how can i help you...")
            stt = "false"
        else:
            say("hmmm, firstly you are not my boss, who are you...")
            count = count+1
        if(count > 2):
            say("surely you are not my boss, call him first then talk to me, I quit...")
            stt = "false"
            st = "false"

    while st == "true":
        print("Listening")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"],
                 ["chat GPT", "https://chat.openai.com/"], ["github", "https://github.com/"],
                 ["whatsapp", "https://web.whatsapp.com/"], ["mail", "https://mail.google.com/mail/u/0/#inbox"],
                 ["wikipedia", "https://www.wikipedia.org/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Sure sir, Opening {site[0]} ...")
                webbrowser.open(site[1])

        musics = [["wedding", r"C:\Users\Paramveer Singh\Music\wedding-121843.mp3"], ["lado", r"C:\Users\Paramveer Singh\Music\Laado_128-(PagalWorld).mp3"]]
        for music in musics:
            if f"play {music[0]}".lower() in query.lower():
                say(f"sure sir, playing {music[0]} song")
                os.startfile(music[1])

        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime} sir..")

        apps = [["spotify", r"C:\Users\Paramveer Singh\AppData\Local\Microsoft\WindowsApps\Spotify.exe"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Sure sir, Opening {app[0]}")
                os.startfile(app[1])

        games = [["need for speed", r"D:\Games\Need for Speed - Most Wanted\NFS13.exe"]]
        for game in games:
            if f"launch {game[0]}".lower() in query.lower():
                say(f"sure sir, launching {game[0]}")
                os.stat(game[1])

        if "shutdown" in query:
            say("Sure sir, when ever you want any help please let me know, have a great time...")
            st = "false"

        #say("I can't understand")
