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
            # checking horizontal
            for i in range(len(board)):
                for j in range(len(board[0])-3):
                    if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                        self.won = True
                        return f"{self.players[board[i][j]-1]} Won Horizontally!"
                    
            # checking vertical
            for i in range(len(board)-3):
                for j in range(len(board[0])):
                    if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                        self.won = True
                        return f"{self.players[board[i][j]-1]} Won Vertically!"
                    
            # checking left to right diagnol
            for i in range(len(board)-3):
                for j in range(len(board[0])-3):
                    if board[i][j] != 0 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                        self.won = True
                        return f"{self.players[board[i][j]-1]} Won Diagnolly!"
            
            # checking right to left diagnol
            for i in range(len(board)-3):
                for j in range(3, len(board[0])):
                    if board[i][j] != 0 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                        self.won = True
                        return f"{self.players[board[i][j]-1]} Won Diagnolly!"
                    
        pos: tuple[int, int] | None = colCheck(col)

        if pos is None:
            return "Column full!"
        
        row , column = pos
        
        self.board[row][column] = self.turn+1
            
        self.printBoard()

        winCheck: str | None = didWin(self.board)
        if winCheck is not None:
            return winCheck
        
        result: str = f" {self.players[self.turn]} had a turn\n"
        self.turn: int = (self.turn + 1) % 2
        return result
    
firstGame: Connect4 = Connect4("Dhyan", "Marcus")

while True:
    ask = int(input(f" {firstGame.players[firstGame.turn]}, Enter column to play: "))
    if ask < 0 or ask > 6:
        print(" Invalid column! Try again.")
        continue
    elif ask == "EXIT":
        print(" Exiting game...")
        break
    print(firstGame.play(ask))
    if firstGame.won:
        break
