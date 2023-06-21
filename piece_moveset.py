class PieceMoveSet:
    def __init__(self, name, turn_color):
        self.name = name
        self.turn = turn_color
        self.moves_list = []

    def pawn_move_set(self, white_locations, black_locations):
        if self.turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[self.name]
            if location[1] == 1:
                self.moves_list.append(location[0], location[1] + 1)
                self.moves_list.append(location[0], location[1] + 2)
                for b in enemies:
                    if enemies[b] in self.moves_list:
                        self.moves_list.remove(enemies[b])
            else:
                self.moves_list.append(location[0], location[1] + 1)
                for b in enemies:
                    if enemies[b] in self.moves_list:
                        self.moves_list.remove(enemies[b])
            for b in enemies:
                if (location[0] + 1, location[1] + 1) == enemies[b] or (location[0] - 1, location[1] + 1) == enemies[b]:
                    self.moves_list.append(enemies[b])
            for w in allies:
                if allies[w] in self.moves_list:
                    self.moves_list = []
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[self.name]
            if location[1] == 1:
                self.moves_list.append(location[0], location[1] + 1)
                self.moves_list.append(location[0], location[1] + 2)
                for b in enemies:
                    if enemies[b] in self.moves_list:
                        self.moves_list.remove(enemies[b])
            else:
                self.moves_list.append(location[0], location[1] + 1)
                for b in enemies:
                    if enemies[b] in self.moves_list:
                        self.moves_list.remove(enemies[b])
            for b in enemies:
                if (location[0] + 1, location[1] + 1) == enemies[b] or (location[0] - 1, location[1] + 1) == enemies[b]:
                    self.moves_list.append(enemies[b])
            for w in allies:
                if allies[w] in self.moves_list:
                    self.moves_list = []

    def rook_move_set(self, white_locations, black_locations):
        if self.turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[self.name]
            
    
