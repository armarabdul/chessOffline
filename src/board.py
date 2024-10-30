 
from pieces import Piece, Pawn, Rook  # Import piece classes

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Set up pawns
        for i in range(8):
            self.grid[1][i] = Pawn('white')
            self.grid[6][i] = Pawn('black')
        # Set up rooks
        self.grid[0][0] = Rook('white')
        self.grid[0][7] = Rook('white')
        self.grid[7][0] = Rook('black')
        self.grid[7][7] = Rook('black')

    def display(self):
        for row in self.grid:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start, end):
        x1, y1 = start
        x2, y2 = end
        piece = self.grid[x1][y1]

        if piece and (x2, y2) in piece.valid_moves((x1, y1)):
            self.grid[x2][y2] = piece
            self.grid[x1][y1] = None
        else:
            print("Invalid move")
