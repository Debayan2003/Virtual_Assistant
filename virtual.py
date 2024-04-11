import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests
import os
import threading
import tkinter as tk
from PIL import Image, ImageTk

# ... Your voice assistant code ...
print('Loading your AI personal assistant - NEW AI')

engine=pyttsx3.init()
voices=engine.getProperty('voices')
zira_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', zira_voice_id)

# Define the function for the assistant
def assistant_listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            statement = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {statement}")
        except Exception as e:
            print("Sorry, I did not understand that.")

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def calculate(statement):
    if 'add' in statement:
        numbers = [int(num) for num in statement.split() if num.isdigit()]
        result = sum(numbers)
        speak(f"The sum is {result}")
        print(f"The sum is {result}")
    elif 'plus' in statement or '+' in statement:
        numbers = [int(num) for num in statement.split() if num.isdigit()]
        result = sum(numbers)  # Define 'result' in this scope
        speak(f"The sum is {result}")
        print(f"The sum is {result}")
    elif 'subtract' in statement or 'minus' in statement or '-' in statement:
        numbers = [int(num) for num in statement.split() if num.isdigit()]
        result = numbers[0] - sum(numbers[1:])
        speak(f"The result is {result}")
        print(f"The result is {result}")
    elif 'multiply' in statement or 'into' in statement:
        numbers = [int(num) for num in statement.split() if num.isdigit()]
        result = 1
        for num in numbers:
            result *= num
        speak(f"The product is {result}")
        print(f"The product is {result}")

def add_event_to_calendar():
    speak("What event and on which date?")
    event_details = takeCommand()
    webbrowser.open_new_tab("https://calendar.google.com/calendar")
    # Note: The assistant can't interact with the webpage, so the user will have to manually add the event.
    speak("Please add your event to the calendar.")
    print("Event saved successfully. What else?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def run_animation():
    root = tk.Tk()
    root.geometry("500x500")
    file = 'newfile.gif'
    info = Image.open(file)
    frames = info.n_frames

    im = []
    for i in range(frames):
        img = Image.open(file)
        img.seek(i)
        img_rgba = img.convert("RGBA")
        photo = ImageTk.PhotoImage(img_rgba)
        im.append(photo)

    gif_label = tk.Label(root, image=im[0])
    gif_label.pack()

    def animation(count):
        if count == frames:
            count = 0
        gif_label.configure(image=im[count])
        count += 1
        root.after(int(50*0.85), lambda: animation(count))

    animation(0)

    root.mainloop()

# ... The rest of your voice assistant code ...
speak("Loading your AI personal assistant - New AI")
wishMe()


if __name__=='__main__': 

    while True:

        speak("Tell me, how can I help you now?")
        # Run the animation in a separate thread
        animation_thread = threading.Thread(target=run_animation)
        animation_thread.start()

        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant New AI is shutting down,Good bye')
            print('your personal assistant New AI is shutting down,Good bye')
            break


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open whatsapp' in statement:
            webbrowser.open_new_tab("https://www.whatsapp.com") or os.system('whatsapp')
            speak("Whatsapp Web is opened now")
            time.sleep(5)

        elif 'open spotify' in statement:
            webbrowser.open_new_tab("https://www.spotify.com") or os.system('spotify')
            speak("spotify web player is opened now")
            time.sleep(5)

        elif 'edge' in statement:
            os.system('start msedge')
            speak("edge browser is opened")
            time.sleep(4)
        elif 'paint' in statement:
            os.system('start mspaint')
            time.sleep(4)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am New AI version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Avilash")
            print("I was built by Avilash")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'add' in statement or 'subtract' in statement or 'minus' in statement or 'multiply' in statement or 'into' or '+' in statement or '-' in statement or 'plus' in statement:
            calculate(statement)

        elif 'add a event in calendar' in statement:
            add_event_to_calendar()

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        # Make sure to join the thread before the program exits
        animation_thread.join() 

time.sleep(3)

