import pyttsx3
import  speech_recognition as sr
from pywin32_testutil import non_admin_error_codes
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio= r.listen(source, timeout= 0,phrase_time_limit=5)
    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# greetings
def wish() :
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('Good morning')
    elif hour>12 and hour<18:
        speak('Good afternoon')
    else:
        speak("good evening")
    speak('I am popii, please tell me how can i help you')
def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('riyasingh5667parihar@gmail.com', 'Riya@1934')
    server.sendmail('riyasingh5667parihar@gmail.com',to,content)
    server.close()

if __name__ == "__main__" :
    wish()
    while True:
      if 1:
         query= takecommand().lower()

         #task work
         if 'open notepad' in query:
             npath = "C:\\Windows\\System32\\notepad.exe"
             os.startfile(npath)
         elif 'open command prompt' in query :
             os.system('start cmd')
         elif 'open camera' in query:
             cap=cv2.VideoCapture(0)
             while True:
                 ret, img= cap.read()
                 cv2.imshow('webcam',img)
                 k= cv2.waitKey(50)
                 if k==27:
                     break;
             cap.release()
             cv2.destroyAllWindows()
         elif 'play music' in query:
             music_dir= "D:\\music"
             songs=os.listdir(music_dir)
             rd= random.choice(songs)
             os.startfile(os.path.join(music_dir,rd))
         elif 'ip address' in query:
             ip=get("https://api.ipify.org").text
             speak(f"your ip address is {ip}")
         elif 'wikipedia' in query:
             speak("searching wikipedia...")
             query= query.replace("wikipedia","")
             results= wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             speak(results)
             print(results)
         elif 'open youtube' in query:
             webbrowser.open("www.youtube.com")
         elif 'open google' in query:
             speak("what should i search on google")
             cm= takecommand().lower()
             webbrowser.open(f"{cm}")
         elif 'send message' in query:
             kit.sendwhatmsg("+919741342399","this is testing protocol",17,57)
         elif 'play song on youtube' in query:
             kit.playonyt("apt")
         elif 'send email' in query:
             try:
                speak('what should i say')
                content=takecommand().lower()
                to="riyasingh56667parihar@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
             except Exception as e:
                 print(e)
                 speak('could not send the email')

         elif 'no thanks' in query:
             speak("thanks for using me have a great day ahead")
             sys.exit()

         speak("is there something else i can do for you")
