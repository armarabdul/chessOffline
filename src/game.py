from board import Board

def main():
    board = Board()
    while True:
        board.display()
        move = input("Enter your move (e.g., 'e2 e4') or 'exit' to quit: ")
        if move.lower() == 'exit':
            break
        start, end = move.split()
        start_pos = (8 - int(start[1]), ord(start[0]) - ord('a'))  # Convert to grid coordinates
        end_pos = (8 - int(end[1]), ord(end[0]) - ord('a'))  # Convert to grid coordinates
        board.move_piece(start_pos, end_pos)

if __name__ == "__main__":
    main()

