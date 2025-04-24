import speech_recognition as sr  # Speech recognition module for voice input
import pyttsx3  # Text-to-speech conversion
from web import CommandProcessor  # CommandProcessor to handle web commands

class Assistant:
    # Assistant class for controlling voice interaction
    def __init__(self, name="Huzaifa"):
        self.engine = pyttsx3.init()  # Initialize the speech engine
        self.name = name  # Set assistant's name (default: "Huzaifa")

    def speak(self, text):
        # Function to speak a given text
        self.engine.say(text)
        self.engine.runAndWait()

    def greet(self):
        # Greet the user when the assistant starts
        self.speak("Hii I am Assistant")
        self.speak("Of Huzaifa Abdulrab")
        self.speak("So, you call me Robert")
        self.speak("What type app open applications...")

class VoiceRecognizer:
    # Voice recognition class to process the speech input
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Initialize the recognizer

        # Adjust energy threshold to ignore background noise

        # Set the energy threshold to filter out low-volume sounds
        self.recognizer.energy_threshold = 5000  
        # Enable dynamic adjustment of energy threshold
        self.recognizer.dynamic_energy_threshold = True

    def listen(self, prompt=""):
        # Listen for the user's speech input
        with sr.Microphone() as source:
            if prompt:
                # Display the prompt message
                print(prompt)  

            # Adjust for ambient noise (background noise) and listen for audio input
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=8)  # Record the audio
            return self.recognizer.recognize_google(audio)  # Convert audio to text using Google's speech recognition

def run_assistant():
    assistant = Assistant()  # Initialize the assistant
    processor = CommandProcessor(assistant)  # CommandProcessor to handle various commands
    recognizer = VoiceRecognizer()  # Initialize the voice recognizer

    assistant.greet()  # Greet the user at the start of the assistant
    active = False  # Flag to track whether the assistant is active and listening for commands

    while True:
        try:
            if not active:
                print("Listening for trigger word...")
                word = recognizer.listen()  # Listen for the trigger word (e.g., "Robert")
                print("Heard:", word)

                if "robert" in word.lower():  # Check if the trigger word is detected
                    assistant.speak("Yes buddy, I'm here. Ready for your command.")
                    active = True  # Set active to True to start listening for commands
            else:
                command = recognizer.listen("Listening for command...")  # Listen for a command
                print("Command:", command)
                if "exit" in command.lower() or "stop" in command.lower():  # Stop listening if "exit" or "stop" is heard
                    assistant.speak("Okay, going offline. Bye!")
                    break  # Break the loop and stop the assistant
                processor.process(command)  # Process the command (open websites, etc.)

        except Exception as e:
            print("Error:", str(e))  # Print any errors that occur during execution

if __name__ == "__main__":
    run_assistant()  # Start the assistant when the script is run
