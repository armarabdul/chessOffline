from src.pieces import Pawn, Rook

def test_pawn_movement():
    pawn = Pawn('white')
    moves = pawn.valid_moves((1, 0))  # Starting position e2 (1, 0)
    assert (2, 0) in moves  # It can move to e3 (2, 0)

def test_rook_movement():
    rook = Rook('white')
    moves = rook.valid_moves((0, 0))  # Starting position a1 (0, 0)
    assert (1, 0) in moves  # Can move to a2
    assert (0, 1) in moves  # Can move to b1

if __name__ == "__main__":
    test_pawn_movement()
    test_rook_movement()
    print("All tests passed!")

