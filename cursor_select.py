import pygame

class CursorSelect:
    def __init__(self, coordinates, turn_color):
        self.mouse_coordinates = coordinates
        self.turn = turn_color

    def determine_piece_from_coordinates(self, white_locations, black_locations, turn, coordinates):
        turn = self.turn
        coordinates = self.mouse_coordinates
        if turn:
            for name in white_locations:
                if coordinates == white_locations[name]:
                    return name
        else:
            for name in black_locations:
                if coordinates == black_locations[name]:
                    return name
    

