import time
# sudoku_board = [
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 7, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8],
#     [0, 0, 8, 5, 0, 0, 0, 1, 0],
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]
# ]
sudoku_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
]

def solve(board:list[list[int]]) -> bool:
    find: tuple[int, int] | None = findEmpty(board)
    if not find:
        return True
    else:
        row, col= find
    for i in range(1,10):
        if isValid(board, i,(row,col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
    return False

def isValid(board:list[list[int]], num:int, pos:tuple) -> bool:
    
    # Checking Row
    for i in range(len(board[0])): 
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Checking Column
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check Box
    box_x:int = pos[1] // 3
    box_y:int = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
            
    return True

def printBoard(board:list[list[int]]) -> None:
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+ " ", end="")

def findEmpty(board:list[list[int]]) -> tuple[int,int] | None:
    count= {}
    for j in range(len(board)):
        for k in range(len(board)):
            if board[j][k] == 0:
                count[(j,k)] = 0
    for i in range(1,10):
        for j in range(len(board)):
            for k in range(len(board)):
                if board[j][k] == 0 and isValid(board, i , (j,k)):
                    count[(j,k)] +=1
    return min(count, key=count.get, default=None) #type: ignore
    
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] == 0:
    #             return (i, j) # row, col

    # return None

print("_________________________")
print()
printBoard(sudoku_board)
start: float = time.time()
solve(sudoku_board)
end: float = time.time()
print("_________________________")
print()
printBoard(sudoku_board)
print("_________________________")
print()
print(f"Took program {(end-start):.3f} seconds to finish.")