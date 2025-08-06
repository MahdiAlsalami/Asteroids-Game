import pygame
import constants
from constants import *
from player import Player

def main():
    pygame.init()
    
    dt = 0
    delta = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = delta.tick(60) / 1000 


        

if __name__ == "__main__":
    main()
