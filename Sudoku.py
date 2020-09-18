board = [
    [2,0,7,0,3,5,0,0,4],
    [6,0,9,0,0,0,0,0,0],
    [0,0,0,0,0,7,0,0,0],
    [7,0,4,9,0,0,6,0,8],
    [3,0,0,0,6,0,0,0,1],
    [1,0,5,0,0,2,7,0,9],
    [0,0,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,9,0,5],
    [4,0,0,5,2,0,1,0,3]
]
def solve(board):#solving the game
    #print(board)#shows step by step solving
    find = find_empty(board)
    if not find:# Found the solution and done
        return True
    else:
        row,column = find

    for i in range(1,10):#go throguh values for each box in the rows
        if valid(board, i, (row,column)):#i is number, parantheses is position, if i is vaild it will continue for the rest
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = 0#reset the previous number inserted
    return False

def valid(board, number, position):#check if the value inserted is vaild
    for i in range(len(board[0])): #Check row
        if board[position[0]][i] == number and position[1] != i: #check if value added is equal to current number
            return False
        
    for i in range(len(board[0])): #Check column
        if board[i][position[1]] == number and position[0] != i: #check if value added is equal to current number
            return False
    box_x = position[1] // 3 #3x3 box
    box_y = position[0] // 3

    for i in range (box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) == position:
                return False
    return True

def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:#after 3rd row prints horizontal line
            print("-----------------------")
        
        for j in range(len(board[0])):#horizontal lines between rows after the 3rd box
            if j % 3 == 0 and j != 0:#checks if it is the 3rd box
                print(" | ", end = "")

            if j == 8:#checks if in the last box
                print(board[i][j])
            else:
                print(str(board[i][j])+ " ", end = "")#stay on the same line

def find_empty(board):#finds empty box 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row,column

display_board(board)#display unsolved board
solve(board)
print('____________________________________________________________')
display_board(board)#display solved board


