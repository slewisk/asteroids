import pygame, time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            
        screen.fill(pygame.Color("Black"))
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if player.collides_with(item):
                print("Game over!")
                pygame.quit()
                return
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    

    


if __name__ == "__main__":
	main()
