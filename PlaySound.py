import pygame
import threading
import time
import os
import base64
import io

class PlaySound():

    def __init__(self) -> None:
        
        self.thread = None
        pygame.init()
        pygame.mixer.init()
          
    def play_sound(self, file_path):
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(10)
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.unload()
                
    def remove_file(self):
        return os.remove('file.mp3')
            
    def play_sound_threaded(self, file_path):

        self.thread = threading.Thread(target=self.play_sound, args=(file_path,))
        self.thread.start()

    def stop_playing(self):
        # pygame.mixer.music.pause()
        # pygame.mixer.quit()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        self.remove_file()
    
    def busy(self):
        return pygame.mixer.music.get_busy()
        
        