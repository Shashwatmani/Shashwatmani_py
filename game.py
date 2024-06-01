def print_board(board):
    """Function to print the current board state"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Function to check if the current player has won"""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Function to check if the game is a draw"""
    return all(cell != " " for row in board for cell in row)

def make_move(board, player, row, col):
    """Function to make a move on the board"""
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def switch_player(player):
    """Function to switch the player"""
    return "O" if player == "X" else "X"

def main():
    """Main function to run the Tik-Tak-Toe game"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter numbers between 0 and 2.")
            continue
        
        if not make_move(board, current_player, row, col):
            print("Cell already taken. Try again.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()
