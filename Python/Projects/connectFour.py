class Connect4():

    def __init__(self, plyr1, plyr2) -> None:
        self.board: list[list[int]] = [[0 for _ in range(7)] for _ in range(6)]
        self.won = False
        self.turn = 0
        self.players = [plyr1, plyr2]
        self.printBoard()
        
    def printBoard(self) -> None:

        print("\n 0   1   2   3   4   5   6")
        print("---------------------------\n")
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if j == 6:
                    print(f" {self.board[i][j]}")
                else:
                    print(f" {self.board[i][j]} |", end="")
            if i != 5:
                print("---------------------------")
        print()
        
    def play(self, col) -> str:
        
        def colCheck(colm) -> tuple[int, int] | None:
            for i in range(len(self.board)-1, -1, -1):
                if self.board[i][colm] == 0:
                    return (i, colm)
            return None
        
        
        def didWin(board) -> str | None:
            return None

        pos: tuple[int, int] | None = colCheck(col)

        if pos is None:
            return "Column full!"
        
        row , column = pos
        
        self.board[row][column] = self.turn+1
            
        winCheck: str | None = didWin(self.board)
        if winCheck is not None:
            return winCheck
        
        self.printBoard()
        
        result: str = f" Player {self.players[self.turn]} has a turn\n"
        self.turn: int = (self.turn + 1) % 2
        return result
    
firstGame: Connect4 = Connect4("Dhyan", "Marcus")

while True:
    ask = int(input(" Enter column to play: "))
    if ask < 0 or ask > 6:
        print(" Invalid column! Try again.")
        continue
    elif ask == "EXIT":
        print(" Exiting game...")
        break
    print(firstGame.play(ask))