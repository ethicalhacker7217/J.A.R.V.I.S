import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import sys
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("good morning!")
    elif 12 <= hour < 18:
        talk("Good Afternoon!")

    else:
        talk("good evening")
    talk("I m Joy ")
    talk(" plz tell how may i help u..")


def take_command():
    try:
        with sr.Microphone()as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'joy' in command:
                command = command.replace('joy', '')
                print(command)

    except:
        pass
    return command

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('cybergenius7217@gmail.com', 'Anshuman@123')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'tushar': 'tushardid123@gmail.com',
    'dad': 'mkmbhu@gmail.com',
    'sis': 'medhamishravns1997@gmail.com',
    'self': 'cybergenius7217@gmail.com',
    'friend': 'iawesomeadi@gmail.com'
}


def run_joy():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is' + time)
    elif 'wikipedia' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'search' in command:
        person = command.replace('search', '')
        webbrowser.open("https://google.com/search?q=" + person)
    elif 'news' in command:
        x = webbrowser.open("https://news.google.com/")
        talk(x)
        print(x)
    elif 'email' in command:
        def get_email_info():
            talk('To Whom you want to send email')
            name = take_command()
            receiver = email_list[name]
            print(receiver)
            talk('What is the subject of your email?')
            subject = take_command()
            talk('Tell me the text in your email')
            message = take_command()
            send_email(receiver, subject, message)
            talk('Email sent....')
            talk('Do you want to send more email?')
            send_more = take_command()
            if 'yes' in send_more:
                get_email_info()

        get_email_info()
        talk('thanks')
        print('thanks')
    elif 'quit' or 'goodbye' or 'sleep' in command:
        print("Have a goodday ahead.... ")
        sys.exit()
    else:
        print("plz repeat it again...")


wishMe()
while True:
    run_joy()
