class Connect4():

    def __init__(self, plyr1, plyr2) -> None:
        self.board: list[list[int]] = [[0 for _ in range(7)] for _ in range(6)]
        self.won = False
        self.tie = False
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
        
    def colCheck(self, colm) -> tuple[int, int] | None:
            for i in range(len(self.board)-1, -1, -1):
                if self.board[i][colm] == 0:
                    return (i, colm)
            return None
    
    def didWin(self) -> str | None:
    
    
    
            # checking horizontal
            for i in range(len(self.board)):
                for j in range(len(self.board[0])-3):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        self.won = True
                        return f"{self.players[self.board[i][j]-1]} Won Horizontally!"
                    
            # checking vertical
            for i in range(len(self.board)-3):
                for j in range(len(self.board[0])):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        self.won = True
                        return f"{self.players[self.board[i][j]-1]} Won Vertically!"
                    
            # checking left to right diagnol
            for i in range(len(self.board)-3):
                for j in range(len(self.board[0])-3):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                        self.won = True
                        return f"{self.players[self.board[i][j]-1]} Won Diagonally!"
            
            # checking right to left diagnol
            for i in range(len(self.board)-3):
                for j in range(3, len(self.board[0])):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                        self.won = True
                        return f"{self.players[self.board[i][j]-1]} Won Diagonally!"
            return None
    
    def didTie(self) -> str | None:
            for i in range(len(self.board)):
                if 0 in self.board[i]:
                    return None
            self.tie = True
            return "Tie, the board is full!"

    def play(self, col) -> str:

        # Column full check
        pos: tuple[int, int] | None = self.colCheck(col)
        if pos is None:
            return "Column full!"


        # Placing the mark
        row , column = pos
        self.board[row][column] = self.turn+1
        self.printBoard()


        # Checking Wins
        winCheck: str | None = self.didWin()
        if winCheck is not None:
            return winCheck
        
        
        # Checking Tie/Draw
        tieCheck: str | None = self.didTie()
        if tieCheck is not None:
            return tieCheck


        # Changing and printing turns
        result: str = f" {self.players[self.turn]} had a turn\n"
        self.turn: int = (self.turn + 1) % 2
        return result
    

def main() -> None:
    player1: str = input("Enter first player's name: ")
    player2: str = input("Enter second player's name: ")

    firstGame: Connect4 = Connect4(player1,player2)

    while True:
        ask = input(f" {firstGame.players[firstGame.turn]}, Enter column to play: ")

        if ask == "EXIT":
            print(" Exiting game...")
            break


        if not ask.isdigit() or int(ask) < 0 or int(ask) > 6:
            print(" Invalid column! Try again.")
            continue
        
        print(firstGame.play(int(ask)))


        if firstGame.won or firstGame.tie:
            break
        
if __name__ == "__main__":
    main()