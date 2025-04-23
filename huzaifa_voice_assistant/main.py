import  speech_recognition as sr
import pywhatkit
import pyttsx3
import webbrowser
import datetime
import os

def start():
    print("Huzaifa Voice Assistant is now running!")
class Assistant:
    
    def __init__(self,name = "Huzaifa"):
        self.engine = pyttsx3.init()
        self.name=name

    def speak(self , text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greet(self):
        self.speak("Hii I am Assistant")
        self.speak("Of Huzaifa Abdulrab")
        self.speak("so you call me robert")
        self.speak("What type app open applications...")

class CommandProcessor:
    def __init__(self, assistant):
        self.assistant = assistant
        
    def process(self, command):
        command = command.lower()

        # Opening websites
        if "google" in command:
            self.assistant.speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "facebook" in command:
            self.assistant.speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "youtube" in command:
            if "play" in command:
                song = command.replace("youtube", "").replace("play", "").strip()
                self.assistant.speak(f"Searching YouTube for {song}")
                pywhatkit.playonyt(song)
            elif "search" in command:
                search = command.replace("youtube", "").replace("search", "").strip()
                self.assistant.speak(f"Searching YouTube for {search}")
                search_url = f"https://www.youtube.com/results?search_query={'+'.join(search.split())}"
                webbrowser.open(search_url)
            else:
                self.assistant.speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
        elif "twitter" in command:
            self.assistant.speak("Opening Twitter")
            webbrowser.open("https://www.twitter.com")
        elif "chat gpt" in command:
            self.assistant.speak("Opening chat gpt")
            webbrowser.open("https://www.chatgpt.com")
        elif "linkedin" in command:
            self.assistant.speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
        elif "instagram" in command:
            self.assistant.speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
        elif "github" in command:
            self.assistant.speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif "reddit" in command:
            self.assistant.speak("Opening Reddit")
            webbrowser.open("https://www.reddit.com")
        elif "quora" in command:
            self.assistant.speak("Opening Quora")
            webbrowser.open("https://www.quora.com")
        elif "wikipedia" in command:
            self.assistant.speak("Opening Wikipedia")
            webbrowser.open("https://www.wikipedia.org")
        elif "amazon" in command:
            self.assistant.speak("Opening Amazon")
            webbrowser.open("https://www.amazon.com")
        elif "ebay" in command:
            self.assistant.speak("Opening eBay")
            webbrowser.open("https://www.ebay.com")
        elif "netflix" in command:
            self.assistant.speak("Opening Netflix")
            webbrowser.open("https://www.netflix.com")
        elif "spotify" in command:
            self.assistant.speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif "telegram" in command:
            self.assistant.speak("Opening Telegram")
            webbrowser.open("https://web.telegram.org")
        elif "twitch" in command:
            self.assistant.speak("Opening Twitch")
            webbrowser.open("https://www.twitch.tv")
        elif "googlemaps" in command:
            self.assistant.speak("Opening Google Maps")
            webbrowser.open("https://www.google.com/maps")
        elif "googledrive" in command:
            self.assistant.speak("Opening Google Drive")
            webbrowser.open("https://drive.google.com")
        elif "dropbox" in command:
            self.assistant.speak("Opening Dropbox")
            webbrowser.open("https://www.dropbox.com")
        elif "zoom" in command:
            self.assistant.speak("Opening Zoom")
            webbrowser.open("https://zoom.us")
        elif "skype" in command:
            self.assistant.speak("Opening Skype")
            webbrowser.open("https://www.skype.com")
        elif "HuzaifaPortfolio" in command:
            self.assistant.speak("Opening huzaifa portfolio")
            webbrowser.open("https://huzaifaabdulrabportfolio.vercel.app")
        elif "microsoft" in command:
            self.assistant.speak("Opening Microsoft")
            webbrowser.open("https://www.microsoft.com")
        elif "apple" in command:
            self.assistant.speak("Opening Apple")
            webbrowser.open("https://www.apple.com")
        elif "google docs" in command:
            self.assistant.speak("Opening Google Docs")
            webbrowser.open("https://docs.google.com")
        elif 'time' in command:
            now = datetime.datetime.now().strftime("%I:%M%P")
            self.assistant.speak(f"The time is {now}")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%B %d , %y")
            self.assistant.speak(f"Today's date is {today}")
        elif 'camera' in command:
            self.assistant.speak("Opening Camera")
            os.system("Start microsoft.windows.camera:")
        else:
            self.assistant.speak("Sorry, I don't recognize that command.")

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        
    def listen(self , prompt = ""):
        with  sr.Microphone() as source:
            if prompt:
                print(prompt)
            audio = self.recognizer.listen(source , timeout=10 , phrase_time_limit=5)
            return self.recognizer.recognize_google(audio)

if __name__ == "__main__":
    assistant = Assistant()
    processor = CommandProcessor(assistant)
    recognizer = VoiceRecognizer()

    assistant.greet()
    active = False

    while True:
        try:
            if not active:
                print("Listening for trigger word...")
                word = recognizer.listen()
                print("Heard:", word)

                if "robert" in word.lower():
                    assistant.speak("Yes buddy, I'm here. Ready for your command.")
                    active = True
            else:
                command = recognizer.listen("Listening for command...")
                print("Command:", command)
                if "exit" in command.lower() or "stop" in command.lower():
                    assistant.speak("Okay, going offline. Bye!")
                    break
                processor.process(command)

        except Exception as e:
            print("Error:", str(e))