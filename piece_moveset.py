class PieceMoveSet:
    def __init__(self, name, turn_color):
        self.name = name
        self.turn = turn_color
        self.moves_list = []
    
    def choose_moves(self, name, white_pieces_locations, black_pieces_locations, moves, turn):
        name = self.name
        white = white_pieces_locations
        black = black_pieces_locations
        moves = self.moves_list
        turn = self.turn
        if "pawn" in name:
            self.pawn_move_set(name=name, white_locations=white, black_locations=black, moves=moves, turn=turn)

    def pawn_move_set(self, name, white_locations, black_locations, moves, turn):
        moves = self.moves_list
        turn = self.turn
        name = self.name
        if turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]
            if location[1] == 1:
                moves(location[0], location[1] + 1)
                moves(location[0], location[1] + 2)
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            else:
                moves.append(location[0], location[1] + 1)
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            for b in enemies:
                if (location[0] + 1, location[1] + 1) == enemies[b] or (location[0] - 1, location[1] + 1) == enemies[b]:
                    moves.append(enemies[b])
            for w in allies:
                if allies[w] in moves:
                    moves = []
            return moves
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]
            if location[1] == 1:
                moves.append(location[0], location[1] + 1)
                moves.append(location[0], location[1] + 2)
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            else:
                moves.append(location[0], location[1] + 1)
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            for b in enemies:
                if (location[0] + 1, location[1] + 1) == enemies[b] or (location[0] - 1, location[1] + 1) == enemies[b]:
                    moves.append(enemies[b])
            for w in allies:
                if allies[w] in moves:
                    moves = []