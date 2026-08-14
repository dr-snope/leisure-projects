import time
import datetime
import pygame

def set_alarm():
    alarm_time = input('Enter target time (HH:MM:SS): ').strip()
    is_running = True
    
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("Alarm.mp3")
    except pygame.error as e:
        print(f"Error loading sound file: {e}")
        return

    print(f"Alarm set! Rings at {alarm_time}")

    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time, end='\r')
        
        if current_time == alarm_time:
            print('\nRISE AND SHINE! 🌞')
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
            is_running = False
            
        time.sleep(1)

if __name__ == '__main__':
    set_alarm()