import pygame, time
from constants import *

def main():
    try:
        pygame.init()
        print(f"Pygame initialized: {pygame.get_init()}")
        print(f"Display driver: {pygame.display.get_driver()}")
    except Exception as e:
        print(f"Error initializing pygame: {e}")
    time.sleep(0.5)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SHOWN | pygame.NOFRAME)
        print("Screen created successfully")
    except Exception as e:
        print(f"Error creating screen: {e}")
    pygame.display.set_caption("Asteroids")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            
        screen.fill(pygame.Color("Black"))
        pygame.display.flip()


if __name__ == "__main__":
	main()
