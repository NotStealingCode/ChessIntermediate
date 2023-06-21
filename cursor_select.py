import pygame

class CursorSelect:
    def __init__(self, coordinates, turn_color):
        self.mouse_coordinates = coordinates
        self.turn = turn_color

    def determine_piece_from_coordinates(self, white_locations, black_locations):
        if self.turn:
            for name in white_locations:
                if self.mouse_coordinates == white_locations[name]:
                    return name
        else:
            for name in black_locations:
                if self.mouse_coordinates == black_locations[name]:
                    return name
    

