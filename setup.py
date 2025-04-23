# setup.py
from setuptools import setup, find_packages

setup(
    name="huzaifa-voice-assistant",
    version="0.2.1",  # Increase this if re-uploading
    author="Huzaifa Abdulrab",
    description="Voice assistant for visually impaired users using speech recognition.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Huzaifaabdulrab/huzaifa-voice-assistant",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "SpeechRecognition",
        "pyttsx3",
        "pyaudio",
        "pywhatkit"
    ],
    entry_points={
        'console_scripts': [
            'huzaifa-voice-assistant=huzaifa_voice_assistant.assistant:run_assistant',
        ],
    },
)
