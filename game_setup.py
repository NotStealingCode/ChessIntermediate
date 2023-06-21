import pygame

COORDINATES = (0, 0)
SIZE = 100
CENTER_X = 20
CENTER_Y = 10

#Board image loaded
board = pygame.image.load("assets/images/cb2.png")


#White pieces images loaded
white_pawn = pygame.image.load("assets/images/pawnw.png")
white_bishop = pygame.image.load("assets/images/bishopw.png")
white_knight = pygame.image.load("assets/images/knightw.png")
white_rook = pygame.image.load("assets/images/rookw.png")
white_queen = pygame.image.load("assets/images/queenw.png")
white_king = pygame.image.load("assets/images/kingw.png")


#Black pieces images loaded
black_pawn = pygame.image.load("assets/images/pawnb.png")
black_bishop = pygame.image.load("assets/images/bishopb.png")
black_knight = pygame.image.load("assets/images/knightb.png")
black_rook = pygame.image.load("assets/images/rookb.png")
black_queen = pygame.image.load("assets/images/queenb.png")
black_king = pygame.image.load("assets/images/kingb.png")


class GameSetUp:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.white_pieces_locations = {
        'white_rook1': (0, 0),
        'white_knight1': (1, 0),
        'white_bishop1': (2, 0),
        'white_queen': (3, 0),
        'white_king': (4, 0),
        'white_bishop2': (5, 0),
        'white_knight2': (6, 0),
        'white_rook2': (7, 0),
        'white_pawn1': (0, 1),
        'white_pawn2': (1, 1),
        'white_pawn3': (2, 1),
        'white_pawn4': (3, 1),
        'white_pawn5': (4, 1),
        'white_pawn6': (5, 1),
        'white_pawn7': (6, 1),
        'white_pawn8': (7, 1),
        }
        self.black_pieces_locations = {
        'black_rook1': (0, 7),
        'black_knight1': (1, 7),
        'black_bishop1': (2, 7),
        'black_queen': (3, 7),
        'black_king': (4, 7),
        'black_bishop2': (5, 7),
        'black_knight2': (6, 7),
        'black_rook2': (7, 7),
        'black_pawn1': (0, 6),
        'black_pawn2': (1, 6),
        'black_pawn3': (2, 6),
        'black_pawn4': (3, 6),
        'black_pawn5': (4, 6),
        'black_pawn6': (5, 6),
        'black_pawn7': (6, 6),
        'black_pawn8': (7, 6),
        }


    def update_pieces(self):
        self.screen.blit(board, COORDINATES)
        for i in self.white_pieces_locations:
            if "rook" in i:
                self.screen.blit(white_rook, (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "knight" in i:
                self.screen.blit(white_knight,
                            (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "bishop" in i:
                self.screen.blit(white_bishop,
                            (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "queen" in i:
                self.screen.blit(white_queen, (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "king" in i:
                self.screen.blit(white_king, (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
            else:
                self.screen.blit(white_pawn, (self.white_pieces_locations[i][0] * SIZE + CENTER_X, self.white_pieces_locations[i][1] * SIZE + CENTER_Y))
        for i in self.black_pieces_locations:
            if "rook" in i:
                self.screen.blit(black_rook, (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "knight" in i:
                self.screen.blit(black_knight,
                            (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "bishop" in i:
                self.screen.blit(black_bishop,
                            (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "queen" in i:
                self.screen.blit(black_queen, (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
            elif "king" in i:
                self.screen.blit(black_king, (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
            else:
                self.screen.blit(black_pawn, (self.black_pieces_locations[i][0] * SIZE + CENTER_X, self.black_pieces_locations[i][1] * SIZE + CENTER_Y))
    
