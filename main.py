import pygame 
from gamesetup import GameSetUp


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

game_set_up = GameSetUp(SCREEN_WIDTH, SCREEN_HEIGHT)
game_set_up.clock.tick(FPS)
game_set_up.update_pieces()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
