class Connect4():

    def __init__(self) -> None:
        self.board: list[list[int]] = [[0 for _ in range(7)] for _ in range(6)]
        self.won = False
        self.turn = 0
    def play(self, col) -> str:
        
        def colCheck(colm) -> tuple[int, int] | None:
            for i in range(len(self.board)-1, -1, -1):
                if self.board[i][colm] == 0:
                    return (i, colm)
            return None
        
        
        def didWin(board) -> str | None:
            pass
            
        if colCheck(col) is None:
            return "Column full!"
        row: int
        column: int
        row, column = colCheck(col)
        self.board[row][column] = str(self.turn+1) 
            
        winCheck: str | None = didWin(self.board)
        if winCheck is not None:
            return winCheck
        
        result: str = f"Player {self.turn+1} has a turn"
        self.turn: int = (self.turn + 1) % 2
        return result
    
