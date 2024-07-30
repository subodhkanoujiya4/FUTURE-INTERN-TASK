def print_board(board):
    print("\n")
    print(" | ".join(board[0]))
    print("-" * 9)
    print(" | ".join(board[1]))
    print("-" * 9)
    print(" | ".join(board[2]))
    print("\n")

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([spot in ['X', 'O'] for row in board for spot in row])

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        while True:
            print_board(board)
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
            if board[row][col] != ' ':
                print("This spot is already taken! Try again.")
                continue
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    tic_tac_toe()
