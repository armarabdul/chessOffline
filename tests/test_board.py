from src.board import Board

def test_board_initialization():
    board = Board()
    assert board.grid[1][0] is not None  # Check if there is a white pawn
    assert board.grid[6][0] is not None  # Check if there is a black pawn

if __name__ == "__main__":
    test_board_initialization()
    print("All tests passed!")
 
