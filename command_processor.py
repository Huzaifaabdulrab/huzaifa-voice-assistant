import datetime
import os
import webbrowser
import urllib.parse
import pywhatkit

class CommandProcessor:
    def __init__(self, assistant):
        self.assistant = assistant
        
    def process(self, command):
        command = command.lower()

        # Opening websites
        if "google" in command:
            if 'search' in command:
                search = command.replace("google","").replace("search","").strip()
                search_encoded = urllib.parse.quote_plus(search)
                self.assistant.speak(f"Searching Google for {search}")
                search_url = f"https://www.google.com/search?q={search_encoded}"
                webbrowser.open(search_url)    
            else:
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
         
        # Adding popular Pakistani websites and apps
        elif "daraz" in command:
            self.assistant.speak("Opening Daraz")
            webbrowser.open("https://www.daraz.pk")
        elif "pakistan news" in command:
            self.assistant.speak("Opening Pakistan News")
            webbrowser.open("https://www.dawn.com")
        elif "urdutimes" in command:
            self.assistant.speak("Opening Urdu Times")
            webbrowser.open("https://www.urdutimes.com")
        elif "jazcash" in command:
            self.assistant.speak("Opening JazzCash")
            webbrowser.open("https://www.jazzcash.com.pk")
        elif "easypaisa" in command:
            self.assistant.speak("Opening EasyPaisa")
            webbrowser.open("https://www.easypaisa.com.pk")
        elif "zameen" in command:
            self.assistant.speak("Opening Zameen")
            webbrowser.open("https://www.zameen.com")
        elif "olx pakistan" in command:
            self.assistant.speak("Opening OLX Pakistan")
            webbrowser.open("https://www.olx.com.pk")
        elif "rozee" in command:
            self.assistant.speak("Opening Rozee.pk")
            webbrowser.open("https://www.rozee.pk")
        elif "pakistan railway" in command:
            self.assistant.speak("Opening Pakistan Railway")
            webbrowser.open("https://www.pakrail.gov.pk")
        elif "telenor" in command:
            self.assistant.speak("Opening Telenor Pakistan")
            webbrowser.open("https://www.telenor.com.pk")
        elif "ptcl" in command:
            self.assistant.speak("Opening PTCL")
            webbrowser.open("https://www.ptcl.com.pk")
        elif "khanewal news" in command:
            self.assistant.speak("Opening Khanewal News")
            webbrowser.open("https://www.khanewalnews.com")
        elif "lahore news" in command:
            self.assistant.speak("Opening Lahore News")
            webbrowser.open("https://www.lahorepulse.com")
        # Adding more global links
        elif "aliexpress" in command:
            self.assistant.speak("Opening AliExpress")
            webbrowser.open("https://www.aliexpress.com")
        elif "etsy" in command:
            self.assistant.speak("Opening Etsy")
            webbrowser.open("https://www.etsy.com")
        elif "yahoo" in command:
            self.assistant.speak("Opening Yahoo")
            webbrowser.open("https://www.yahoo.com")
        elif "bbc" in command:
            self.assistant.speak("Opening BBC News")
            webbrowser.open("https://www.bbc.com")
        elif "cnn" in command:
            self.assistant.speak("Opening CNN")
            webbrowser.open("https://www.cnn.com")
        elif "nytimes" in command:
            self.assistant.speak("Opening New York Times")
            webbrowser.open("https://www.nytimes.com")
        elif "reddit" in command:
            self.assistant.speak("Opening Reddit")
            webbrowser.open("https://www.reddit.com")
        elif "tesla" in command:
            self.assistant.speak("Opening Tesla")
            webbrowser.open("https://www.tesla.com")
        elif "bbc sport" in command:
            self.assistant.speak("Opening BBC Sport")
            webbrowser.open("https://www.bbc.com/sport")
        elif "un" in command:
            self.assistant.speak("Opening United Nations")
            webbrowser.open("https://www.un.org")
        elif "world health organization" in command:
            self.assistant.speak("Opening WHO")
            webbrowser.open("https://www.who.int")
        elif "reddit" in command:
            self.assistant.speak("Opening Reddit")
            webbrowser.open("https://www.reddit.com")
        else:
            self.assistant.speak("Sorry, I don't recognize that command.")
