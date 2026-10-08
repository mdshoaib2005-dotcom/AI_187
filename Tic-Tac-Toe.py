board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"

for i in range(9):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    pos = int(input("Enter position: ")) - 1
    board[pos] = player

    if player == "X":
        player = "O"
    else:
        player = "X"
