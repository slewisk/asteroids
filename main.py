import pygame, time
from constants import *
from player import Player

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0    
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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            
        screen.fill(pygame.Color("Black"))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
	main()
