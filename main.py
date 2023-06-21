import pygame 
from game_setup import GameSetUp
from cursor_select import CursorSelect

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
white_turn = True

game_set_up = GameSetUp(SCREEN_WIDTH, SCREEN_HEIGHT)
game_set_up.clock.tick(FPS)
game_set_up.update_pieces()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = (event.pos[0] // 100, event.pos[1] // 100)
            cursor_select = CursorSelect(coordinates=coordinates, turn_color=white_turn)
            piece_name = cursor_select.determine_piece_from_coordinates(game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, white_turn, coordinates)
            print(coordinates)
            print(piece_name)


    pygame.display.flip()


pygame.quit()
