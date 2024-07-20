import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import wikipedia
import smtplib


Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',200)
def Speak(audio):
    print(' ')
    Assistant.say(audio)
    print(' ')
    Assistant.runAndWait()


def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print('Listening')
        #print(command)
        command.pause_threshold=1
        audio=command.listen(source)
        try:
            print('Recognizing.....')
            query=command.recognize_google(audio,language='en-in')
            print(f"You said :{query}")
        except Exception as Error:
            print("say that again")
            return "None"
        return query.lower()




def sendEmail(to,subject):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('mehulkubba@gmail.com','Mehulmadarchod')
        server.sendmail('mehulkubba@gmail.com',to,content)
        server.close()
Speak("Hi Mehul, I am Jarvis, How can I assist you ?")

while True:
    query=takecommand()
    if 'wikipedia' in query:
        Speak('Searching wikipedia')
        query=query.replace("Jarvis","")
        query=query.replace("wikipedia","")
        wiki=wikipedia.summary(query,2)
        Speak(f"According to the wikipedia: {wiki}")
    elif 'open youtube' in query:
        webbrowser.open('https://www.youtube.com/watch?v=')
    elif 'open google' in query:
        webbrowser.open('https://www.google.com')
    elif 'open stackoverflow' in query:
        webbrowser.open('www.stackoverflow.com')
    elif 'play music' in query:
        webbrowser.open('spotify.com')
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        Speak(f"Sir the time is {strTime}")
    elif 'open code' in query:
        codePath = "C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codePath)
    elif 'email to aditya' in query:
        try:
            Speak('what should i say?')
            content=takecommand()
            to = "aryanaditya3337@gmail.com"
            sendEmail(to,content)
            Speak("Email has been sent")
        except Exception as e:
            print(e)
            Speak('Sorry mehul i am not able to send the mail')