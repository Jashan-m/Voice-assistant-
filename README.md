# Voice-assistant-
A voice Assistant is created using python where you can operate your computer with your voice commands

## Voice-Controlled Assistant
This Python script enables voice-controlled interaction with a computer, offering functionalities such as opening applications, browsing websites, searching for movies, and performing system tasks like adjusting volume,opening inbuilt applications and closing web tabs.

### Key Features:
- **Speech Recognition**: Utilizes the `speech_recognition` library to interpret voice commands.
- **Text-to-Speech**: Uses `pyttsx3` for auditory feedback on command execution.
- **Application Management**: Opens specified applications (`notepad`, `calculator`, `camera`) and handles unrecognized application requests.
- **Web Browsing**: Navigates to predefined websites (`YouTube`, `Instagram`, `Whizrobo`) and conducts web searches based on user input.
- **System Operations**: Includes commands for adjusting system volume and closing browser tabs.

### Usage:
1. **Initialization**: Initializes speech recognition and sets up text-to-speech settings.
2. **Command Handling**: Listens for user commands, executes corresponding actions, and provides verbal feedback.

### Requirements:
- Python 3.x
- Libraries: `speech_recognition`, `pyttsx3`, `webbrowser`, `subprocess`, `pyautogui`,`os`

### Notes:
- Extendable: Easily add more applications or commands as needed.
- Platform Compatibility: Primarily designed for Windows; adaptations may be required for other operating systems.
