class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color[0].upper()}{self.__class__.__name__[0]}"

class Pawn(Piece):
    def valid_moves(self, position):
        moves = []
        direction = 1 if self.color == 'white' else -1
        x, y = position
        if 0 <= x + direction < 8:
            moves.append((x + direction, y))  # Move forward
        return moves

class Rook(Piece):
    def valid_moves(self, position):
        moves = []
        x, y = position
        # Horizontal and vertical moves
        for i in range(8):
            if i != x:
                moves.append((i, y))  # Vertical moves
            if i != y:
                moves.append((x, i))  # Horizontal moves
        return moves

# Add additional pieces (Knight, Bishop, Queen, King) similarly

