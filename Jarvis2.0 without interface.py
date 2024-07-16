import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import pyautogui
import os


# Initialize speech recognition
r = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

# Set voice and rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Define a function to handle user commands
def handle_command(command):
    # Convert command to lowercase
    command = command.lower()
    



    # Handle basic commands
    if 'press start button' in command:
        engine.say('Start button pressed')
        pyautogui.press('alt'+'f4')
    elif 'open application' in command:
        engine.say('Which application would you like to open?')
        engine.runAndWait()
        application = listen_for_command()
        engine.say(f'Opening {application}')
        engine.runAndWait()
        try:
            # Map common application names to their executable paths
            app_paths = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "camera": "camera.exe",

                                
                # Add more applications as needed
            }
            if application in app_paths:
                subprocess.Popen(app_paths[application])
            else:
                engine.say(f'{application} not found in predefined applications')
        except Exception as e:
            engine.say(f'Error opening {application}: {str(e)}')
        engine.runAndWait()
    elif 'open youtube' in command:
        engine.say('Opening YouTube')
        webbrowser.open('https://www.youtube.com/')
        engine.runAndWait()
    elif 'open instagram' in command:
        engine.say('Opening Instagram')
        webbrowser.open('https://www.instagram.com/')
        engine.runAndWait()
    elif 'open whizrobo' in command:
        engine.say('Opening Whizrobo Webpage')
        webbrowser.open('https://whizrobo.com/')
        engine.runAndWait()
    
    elif 'search movie' in command:
        engine.say('What movie would you like to search for?')
        engine.runAndWait()
        movie = listen_for_command()
        engine.say(f'Searching for {movie}')
        webbrowser.open(f'https://www.google.com/search?q={movie}+movie')
        engine.runAndWait()
    elif 'increase volume' in command:
        engine.say('Increasing volume')
        # Placeholder for volume increase code, platform-specific
        os.system("nircmd.exe changesysvolume 2000")  # Example for Windows
        engine.runAndWait()
    elif 'close tabs' in command:
        engine.say('Closing tabs')
        pyautogui.hotkey('ctrl', 'w')  # Assuming this is for closing browser tabs
        engine.runAndWait()
    else:
        engine.say('Sorry, I did not understand that command')
        engine.runAndWait()

# Define a function to listen for user commands
def listen_for_command():
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-US')
            print(f'You said: {command}')
            return command
        except sr.UnknownValueError:
            print('Sorry, I did not understand that')
            engine.say('Sorry, I did not understand that')
            engine.runAndWait()
        except sr.RequestError as e:
            print(f'Error: {e}')
            engine.say(f'Error: {e}')
            engine.runAndWait()
    return ''

# Main loop
if __name__ == '__main__':
    
    while True:
        command = listen_for_command()
        handle_command(command)
        engine.runAndWait()
