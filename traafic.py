import pygame
import time

# Pygame initialize karein
pygame.init()
pygame.mixer.init()

# Screen setup (800x600 resolution)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Signal Light - 3 Lights Simulation (Red, Yellow, Green)")

RED_IMAGE_FILE = "red.png"
YELLOW_IMAGE_FILE = "yellow.png"
GREEN_IMAGE_FILE = "green.png"

RED_AUDIO_FILE = "red.mp3"
YELLOW_AUDIO_FILE = "yellow.mp3"
GREEN_AUDIO_FILE = "green.mp3"


try:
    red_img = pygame.transform.scale(pygame.image.load(RED_IMAGE_FILE), (800,600))
    yellow_img = pygame.transform.scale(pygame.image.load(YELLOW_IMAGE_FILE), (800, 600))
    green_img = pygame.transform.scale(pygame.image.load(GREEN_IMAGE_FILE), (800, 600))
except Exception as e:
    print("Image load karne mein error aayi! Check karein ki teeno images folder mein hain.")
    print("Error:", e)
    exit()


try:
    red_sound = pygame.mixer.Sound(RED_AUDIO_FILE)
    yellow_sound = pygame.mixer.Sound(YELLOW_AUDIO_FILE)
    green_sound = pygame.mixer.Sound(GREEN_AUDIO_FILE)
except Exception as e:
    print("Audio load karne mein error aayi! Check karein ki teeno MP3 files folder mein hain.")
    print("Error:", e)
    exit()

def run_signal_sequence(image, sound, duration, phase_name):
    print(f"[{phase_name}] Signal Active")
    sound.play()  
    
    start_time = time.time()
    clock = pygame.time.Clock()
    
    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit karne ke liye
                
        screen.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(30)
        
    return True

def main():
    print("\n--- 3-Light Signal Simulation Shuru Ho Chuki Hai ---")
    print("Window band karne ke liye 'X' button dabayein.\n")
    
    running = True
    while running:
        # 1. Red Signal (30 Seconds)
        if not run_signal_sequence(red_img, red_sound, 30, "🔴 RED"): break
        
        # 2. Yellow Signal - Going to Green (10 Seconds)
        if not run_signal_sequence(yellow_img, yellow_sound, 10, "🟡 YELLOW (Get Ready)"): break
        
        # 3. Green Signal (40p Seconds)
        if not run_signal_sequence(green_img, green_sound, 60, "🟢 GREEN"): break
        
    
        if not run_signal_sequence(yellow_img, yellow_sound, 10, "🟡 YELLOW (Slow Down)"): break

    pygame.quit()

if __name__ == "__main__":
    main()