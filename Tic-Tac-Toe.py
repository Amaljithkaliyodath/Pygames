# Define the game board
board = [[" " for _ in range(3)] for _ in range(3)]

# Define the game loop
while True:
    # Print the game board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

    # Get the user's move
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))
    board[row][col] = "X"

    # Check if the user has won
    if (board[0][0] == board[0][1] == board[0][2] != " " or
        board[1][0] == board[1][1] == board[1][2] != " " or
        board[2][0] == board[2][1] == board[2][2] != " " or
        board[0][0] == board[1][0] == board[2][0] != " " or
        board[0][1] == board[1][1] == board[2][1] != " " or
        board[0][2] == board[1][2] == board[2][2] != " " or
        board[0][0] == board[1][1] == board[2][2] != " " or
        board[0][2] == board[1][1] == board[2][0] != " "):
        print("You have won!")
        break

    # Check if the board is full
    if " " not in [cell for row in board for cell in row]:
        print("The game is a draw.")
        break

    # Make the computer's move
    import random
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != " ":
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = "O"

    # Check if the computer has won
    if (board[0][0] == board[0][1] == board[0][2] != " " or
        board[1][0] == board[1][1] == board[1][2] != " " or
        board[2][0] == board[2][1] == board[2][2] != " " or
        board[0][0] == board[1][0] == board[2][0] != " " or
        board[0][1] == board[1][1] == board[2][1] != " " or
        board[0][2] == board[1][2] == board[2][2] != " " or
        board[0][0] == board[1][1] == board[2][2] != " " or
        board[0][2] == board[1][1] == board[2][0] != " "):
        print("Computer has won!")
        break

    # Check if the board is full
    if " " not in [cell for row in board for cell in row]:
        print("The game is a draw.")
        break