import pygame
from game_setup import GameSetUp
from cursor_select import CursorSelect
from piece_moveset import PieceMoveSet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
white_turn = True
check = False
black_turn = False
current_choices = []
king_danger_threats = []


game_set_up = GameSetUp(SCREEN_WIDTH, SCREEN_HEIGHT)
game_set_up.clock.tick(FPS)


running = True
while running:
    game_set_up.update_pieces()
    game_set_up.draw_moves(current_choices, white_turn)
    game_set_up.draw_check(king_danger_threats, white_turn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = (event.pos[0] // 100, event.pos[1] // 100)
            cursor_select = CursorSelect(coordinates=coordinates, turn_color=white_turn)
            piece_name = cursor_select.determine_piece_from_coordinates(game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, white_turn, coordinates)
            print(piece_name)
            if piece_name is not None and white_turn:
                for b in game_set_up.black_pieces_locations:
                    king_move_set = PieceMoveSet(b)
                    possible_threats = king_move_set.choose_moves(b, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, king_move_set.moves_list, black_turn)
                    king_danger_threats = king_danger_threats + possible_threats
                piece_move_set = PieceMoveSet(piece_name)
                moves = piece_move_set.choose_moves(piece_move_set.name, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, piece_move_set.moves_list, white_turn)
                game_set_up.draw_moves(moves, white_turn)
                current_choices = moves
                piece_to_be_updated = piece_name
            if coordinates in current_choices and white_turn:
                game_set_up.update_locations(piece_to_be_updated, coordinates, white_turn)
                current_choices = []
                king_danger_threats = []
                white_turn = False
                black_turn = True
            if piece_name is not None and not white_turn:

                current_choices = []
                b_piece_move_set = PieceMoveSet(piece_name)
                moves = b_piece_move_set.choose_moves(b_piece_move_set.name, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, piece_move_set.moves_list, white_turn)
                game_set_up.draw_moves(moves, white_turn)
                current_choices = moves
                piece_to_be_updated = piece_name
            if coordinates in current_choices and not white_turn:
                game_set_up.update_locations(piece_to_be_updated, coordinates, white_turn)
                current_choices = []
                king_danger_threats = []
                for w in game_set_up.white_pieces_locations:
                    king_move_set = PieceMoveSet(w)
                    possible_threats = king_move_set.choose_moves(w, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, king_move_set.moves_list, black_turn)
                    king_danger_threats = king_danger_threats + possible_threats
                white_turn = True
                black_turn = False
    pygame.display.flip()


pygame.quit()
