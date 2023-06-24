class PieceMoveSet:
    def __init__(self, name):
        self.name = name
        self.moves_list = [] 
    def choose_moves(self, name, white_pieces_locations, black_pieces_locations, moves, turn):
        match name:
            case name if "pawn" in name:
                moves1 = self.pawn_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1
            case name if "rook" in name:
                moves1 = self.rook_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1
            case name if "bishop" in name:
                moves1 = self.bishop_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1
            case name if "knight" in name:
                moves1 = self.knight_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1
            case name if "queen" in name:
                moves1 = self.queen_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1
            case name if "king" in name:
                moves1 = self.king_move_set(name, white_pieces_locations, black_pieces_locations, moves, turn)
                return moves1

    def pawn_move_set(self, name, white_locations, black_locations, moves, turn):
        moves = self.moves_list
        white_turn = turn
        name = self.name
        if white_turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]

            if location[1] == 1:
                moves.append((location[0], location[1] + 1))
                moves.append((location[0], location[1] + 2))
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            else:
                moves.append((location[0], location[1] + 1))
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            for b in enemies:
                if (location[0] + 1, location[1] + 1) == enemies[b] or (location[0] - 1, location[1] + 1) == enemies[b]:
                    moves.append(enemies[b])
            for w in allies:
                if allies[w] in moves:
                    moves = []

        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]
            if location[1] == 6:
                moves.append((location[0], location[1] - 1))
                moves.append((location[0], location[1] - 2))
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            else:
                moves.append((location[0], location[1] - 1))
                for b in enemies:
                    if enemies[b] in moves:
                        moves.remove(enemies[b])
            for b in enemies:
                if (location[0] - 1, location[1] - 1) == enemies[b] or (location[0] + 1, location[1] - 1) == enemies[b]:
                    moves.append(enemies[b])
            for w in allies:
                if allies[w] in moves:
                    moves = []
        return moves


    def rook_move_set(self, name, white_locations, black_locations, moves, turn):
        moves = self.moves_list
        white_turn = turn
        name = self.name
        moves1 = []
        moves2 = []
        moves3 = []
        moves4 = []

        if white_turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]
        
            for i in range(0, location[0]):
                moves1.append((location[0] - i - 1, location[1]))
                current_index = moves1.index((location[0] - 1, location[1]))
                if moves1[current_index] in enemies.values():
                    break

            for n in moves1:
                if n in allies.values():
                    current_index = moves1.index(n)
                    moves1 = moves1[:current_index]
                    break
            
                            
            for i in range(location[0] + 1, 8):
                moves2.append((i, location[1]))
                current_index = moves2.index((i , location[1]))
                if moves2[current_index] in enemies.values():
                    break
                

            for n in moves2:
                if n in allies.values():
                    current_index = moves2.index(n)
                    moves2 = moves2[:current_index]
                    break

            for i in range(0, location[1]):
                moves3.append((location[0], i))
                current_index = moves3.index((location[0], i))
                if moves3[current_index] in enemies.values():
                    break
                
            moves3 = moves3[::-1]
            for n in moves3:
                if n in allies.values():
                    current_index = moves3.index(n)
                    moves3 = moves3[:current_index]
                    break
                        
            for i in range(location[1] + 1, 8):
                moves4.append((location[0], i))
                current_index = moves4.index((location[0], i))
                if moves4[current_index] in enemies.values():
                    break

            for n in moves4:
                if n in allies.values():
                    current_index = moves4.index(n)
                    moves4 = moves4[:current_index]
                    break


            moves = moves1 + moves2 + moves3 + moves4
            return moves
        
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]

            for i in range(0, location[0]):
                moves1.append((location[0] - i - 1, location[1]))
                current_index = moves1.index((location[0] - 1, location[1]))
                if moves1[current_index] in enemies.values():
                    break

            for n in moves1:
                if n in allies.values():
                    current_index = moves1.index(n)
                    moves1 = moves1[:current_index]
                    break
            
                            
            for i in range(location[0] + 1, 8):
                moves2.append((i, location[1]))
                current_index = moves2.index((i , location[1]))
                if moves2[current_index] in enemies.values():
                    break
                

            for n in moves2:
                if n in allies.values():
                    current_index = moves2.index(n)
                    moves2 = moves2[:current_index]
                    break

            for i in reversed(range(0, location[1])):
                moves3.append((location[0], i))
                current_index = moves3.index((location[0], i))
                if moves3[current_index] in enemies.values():
                    break
                
            # moves3 = moves3[::-1]
            for n in moves3:
                if n in allies.values():
                    current_index = moves3.index(n)
                    moves3 = moves3[:current_index]
                    break
                        
            for i in range(location[1] + 1, 8):
                moves4.append((location[0], i))
                current_index = moves4.index((location[0], i))
                if moves4[current_index] in enemies.values():
                    break

            for n in moves4:
                if n in allies.values():
                    current_index = moves4.index(n)
                    moves4 = moves4[:current_index]
                    break


            moves = moves1 + moves2 + moves3 + moves4
            return moves
            

    def bishop_move_set(self, name, white_locations, black_locations, moves, turn):
        moves = self.moves_list
        white_turn = turn
        name = self.name
        moves1 = []
        moves2 = []
        moves3 = []
        moves4 = []



        if white_turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]
        
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]

        x_coordinate = location[0]
        y_coordinate = location[1]

        while 0 <= x_coordinate < 7 and 0 <= y_coordinate < 7:
            x_coordinate += 1
            y_coordinate += 1
            if ((x_coordinate, y_coordinate)) in allies.values():
                break
            if ((x_coordinate, y_coordinate)) in enemies.values():
                moves1.append((x_coordinate, y_coordinate))
                break
            else:
                moves1.append((x_coordinate, y_coordinate))                


        x_coordinate = location[0]
        y_coordinate = location[1]
        while 0 <= x_coordinate < 7 and 0 < y_coordinate <= 7:
            x_coordinate += 1
            y_coordinate -= 1
            if ((x_coordinate, y_coordinate)) in allies.values():
                break
            if ((x_coordinate, y_coordinate)) in enemies.values():
                moves2.append((x_coordinate, y_coordinate))
                break
            else:
                moves2.append((x_coordinate, y_coordinate))

        x_coordinate = location[0]
        y_coordinate = location[1]
        while 0 < x_coordinate <= 7 and 0 <= y_coordinate < 7:
            x_coordinate -= 1
            y_coordinate += 1
            if ((x_coordinate, y_coordinate)) in allies.values():
                break
            if ((x_coordinate, y_coordinate)) in enemies.values():
                moves3.append((x_coordinate, y_coordinate))
                break
            else:
                moves3.append((x_coordinate, y_coordinate))

        x_coordinate = location[0]
        y_coordinate = location[1]
        while 0 < x_coordinate <= 7 and 0 < y_coordinate <= 7:
            x_coordinate -= 1
            y_coordinate -= 1
            if ((x_coordinate, y_coordinate)) in allies.values():
                break
            if ((x_coordinate, y_coordinate)) in enemies.values():
                moves4.append((x_coordinate, y_coordinate))
                break
            else:
                moves4.append((x_coordinate, y_coordinate))

        moves = moves1 + moves2 + moves3 + moves4
        return moves

    def knight_move_set(self, name, white_locations, black_locations, moves, turn):        
        moves = self.moves_list
        white_turn = turn
        name = self.name
        moves1 = []
        if white_turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]

        moves1.append((location[0] + 2, location[1] + 1))
        moves1.append((location[0] + 2, location[1] - 1))
        moves1.append((location[0] + 1, location[1] + 2))
        moves1.append((location[0] + 1, location[1] - 2))
        moves1.append((location[0] - 2, location[1] + 1))
        moves1.append((location[0] - 2, location[1] - 1))
        moves1.append((location[0] - 1, location[1] + 2))
        moves1.append((location[0] - 1, location[1] - 2))
        moves2 = []
        for n in moves1:
            if n not in allies.values():
                moves2.append(n)
            
        moves = [(value, key) for (value, key) in moves2 if key >= 0 and key <= 7 and value >= 0 and value <= 7]
        return moves

    def king_move_set(self, name, white_locations, black_locations, moves, turn):
        moves = self.moves_list
        white_turn = turn
        name = self.name
        moves1 = []
        if white_turn:
            allies = white_locations
            enemies = black_locations
            location = white_locations[name]
        
        else:
            allies = black_locations
            enemies = white_locations
            location = black_locations[name]



        moves1.append((location[0] + 1, location[1] + 1))
        moves1.append((location[0] + 1, location[1] - 1))
        moves1.append((location[0] + 1, location[1]))
        moves1.append((location[0] - 1, location[1] - 1))
        moves1.append((location[0] - 1, location[1] + 1))
        moves1.append((location[0] - 1, location[1]))
        moves1.append((location[0], location[1] + 1))
        moves1.append((location[0], location[1] - 1))

        moves2 = []
        for n in moves1:
            print("done")
            if n not in allies.values():
                moves2.append(n)

        moves = [(value, key) for (value, key) in moves2 if key >= 0 and key <= 7 and value >= 0 and value <= 7]
        print(allies.values())
        return moves
        
    def queen_move_set(self, name, white_locations, black_locations, moves, turn):
        white_turn = turn
        moves1 = self.bishop_move_set(name, white_locations, black_locations, moves, turn)
        moves2 = self.rook_move_set(name, white_locations, black_locations, moves, turn)
        moves3 = moves1 + moves2
        return moves3
    
