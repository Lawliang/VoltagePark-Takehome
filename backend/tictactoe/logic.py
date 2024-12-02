def check_winner(board):
    winCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6],             # Diagonals
    ]
    for combo in winCombinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]