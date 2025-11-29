import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    
    audio = r.listen(source)
    print("Audio captured. Processing...")

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Speech recognition could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

