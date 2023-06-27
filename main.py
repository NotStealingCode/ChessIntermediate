import pygame
from game_setup import GameSetUp
from cursor_select import CursorSelect
from piece_moveset import PieceMoveSet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
is_white_turn = True
check = False
black_turn = False
is_deleted = False
current_choices = []
king_danger_threats = []
enemies_moveset = {}
game_set_up = GameSetUp(SCREEN_WIDTH, SCREEN_HEIGHT)
game_set_up.clock.tick(FPS)

move_on = True
running = True
while running:
    move_on = True
    game_set_up.update_pieces()
    game_set_up.draw_moves(current_choices, is_white_turn)
    game_set_up.draw_check(king_danger_threats, is_white_turn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = (event.pos[0] // 100, event.pos[1] // 100)
            cursor_select = CursorSelect(coordinates=coordinates, turn_color=is_white_turn)
            piece_name = cursor_select.determine_piece_from_coordinates(game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, is_white_turn, coordinates)
            if piece_name is not None and is_white_turn:
                piece_move_set = PieceMoveSet(piece_name)
                moves = piece_move_set.choose_moves(piece_move_set.name, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, piece_move_set.moves_list, is_white_turn)
                game_set_up.draw_moves(moves, is_white_turn)
                current_choices = moves
                piece_to_be_updated = piece_name
            if coordinates in current_choices and is_white_turn:
                enemies_moveset = {}
                king_danger_threats = []
                old_location = game_set_up.white_pieces_locations[piece_to_be_updated]
                game_set_up.update_locations(piece_to_be_updated, coordinates, is_white_turn)
                if coordinates in game_set_up.black_pieces_locations.values():
                    deleted_piece = game_set_up.delete_piece(coordinates, is_white_turn)
                    is_deleted = True
                    print(deleted_piece)
                for b in game_set_up.black_pieces_locations:
                    king_move_set = PieceMoveSet(b)
                    possible_threats = king_move_set.choose_moves(b, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, king_move_set.moves_list, black_turn)
                    if game_set_up.white_pieces_locations["white_king"] in possible_threats:
                        enemies_moveset[b] = possible_threats
                        move_on = False
                if enemies_moveset:
                    game_set_up.update_locations(piece_to_be_updated, old_location, is_white_turn)
                    if is_deleted:
                        game_set_up.black_pieces_locations[deleted_piece[0]] = deleted_piece[1]
                print(enemies_moveset)
                if move_on:
                    enemies_moveset = {}
                    current_choices = []
                    king_danger_threats = []
                    is_white_turn = False
                    black_turn = True
                    is_deleted = False
            if piece_name is not None and not is_white_turn:
                current_choices = []
                b_piece_move_set = PieceMoveSet(piece_name)
                moves = b_piece_move_set.choose_moves(b_piece_move_set.name, game_set_up.white_pieces_locations, game_set_up.black_pieces_locations, piece_move_set.moves_list, is_white_turn)
                game_set_up.draw_moves(moves, is_white_turn)
                current_choices = moves
                piece_to_be_updated = piece_name
            if coordinates in current_choices and not is_white_turn:
                game_set_up.update_locations(piece_to_be_updated, coordinates, is_white_turn)
                game_set_up.delete_piece(coordinates, is_white_turn)
                current_choices = []
                king_danger_threats = []
                is_white_turn = True
                black_turn = False
    pygame.display.flip()


pygame.quit()
