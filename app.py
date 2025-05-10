from flask import Flask, render_template, request
import main  
from web import CommandProcessor  # CommandProcessor to handle web commands

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/speak', methods=['POST'])
def speak():
    try:
        assistant = main.Assistant()
        recognizer = main.VoiceRecognizer()
        processor = main.CommandProcessor(assistant)

        assistant.greet()
        command = recognizer.listen("Listening from Web UI")
        print("Command:", command)

        if "stop" in command.lower():
            assistant.speak("Okay, exiting...")
            return {"message": "Assistant stopped."}

        processor.process(command)
        return {"message": f"Processed: {command}"}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)
