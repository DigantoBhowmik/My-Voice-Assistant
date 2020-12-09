import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your sara')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()


    except:
        pass
    return command

def run_sara():
    commands = take_command()
    if 'play' in commands:
        commands = commands.replace('play', '')
        talk('playing' + commands)
        pywhatkit.playonyt(commands)
    elif 'time' in commands:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'are you single' in commands:
        talk('No, I am in a relationship with my computer')
    elif 'how are you' in commands:
        talk('i am good and you?')
    elif 'i love you' in commands:
        talk('sorry, i am not a girl. I am bot')
    elif 'i am also good' in commands:
        talk('okay, how can i help you?')
    elif 'i miss you' in commands:
        talk('uhh,i also miss you')

    elif 'open stackoverflow' in commands:
        webbrowser.open("stackoverflow.com")
    else:
        talk('I can not listen you')

while True:
    run_sara()