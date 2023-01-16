import speech_recognition as sr
import datetime
import threading 
import time
import os
import gtts
from playsound import playsound
from openai_module import Openai_Model
from pydub import AudioSegment
import soundfile as sf
import pyrubberband as pyrb
from pygame import mixer
from pydub import AudioSegment
import multiprocessing
import PlaySound

ai = Openai_Model()
r = sr.Recognizer()
result = 0
soundfilename = 'file.mp3'
sound = PlaySound.PlaySound()

def speed_change(speed=1.15):
    sound = AudioSegment.from_file(soundfilename)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)})
    sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate).export(soundfilename)

def say(text):
    tts = gtts.gTTS(text, lang="en")
    try:
        if sound.busy():
            sound.stop_playing()
        with open(soundfilename, 'w') as f:
            tts.save(soundfilename)
    except:
        say(text)
        
    speed_change()
    sound.play_sound_threaded(soundfilename)
    

def recognize_text(audio_text):  
    response = r.recognize_google(audio_text, language="en-EN", show_all=True)
    text = ""
    if len(response) != 0:
        try:
            text = response['alternative'][0]['transcript']
        except:
            text = ""
        return text
    else:
        return None

def proceduj_dalej(tekst):
    lista = ['pc']
    try:
        if tekst.split(' ')[0].lower() in lista:
            if tekst.lower().find("close the program") != -1:
                say("Closing the program. Bye")
                exit()
        else:
            ai_response = ai.ask_question(tekst)
            print(ai_response)
            say(ai_response)    
    except Exception as e:
        pass

def voice():
    global result
    while True: 
        result = ""
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                result = recognize_text(audio_text)
                if result != None:
                    proceduj_dalej(result)
            except Exception as e:
                continue
        


t1 = threading.Thread(target=voice)
t1.start()
     
    
