maze = [ [0, 1, 1, 0, 0], #0
         [0, 0, 0, 1, 0], #1
         [0, 1, 0, 1, -1], #2
         [0, 1, 1, 1, 0], #3
         [0, 0, 0, 0, 0] ] #4

def print_maze():
    for row in maze:
        print(row)
    print()

column = 0 # x
row = 0 # y
def move_up():
    global row
    row -= 1
    maze[row][column] = 2
    print_maze()

def move_down():
    global row
    row += 1
    maze[row][column] = 2
    print_maze()

def move_left():
    global column
    column -= 1
    maze[row][column] = 2
    print_maze()

def move_right():
    global column
    column += 1
    maze[row][column] = 2
    print_maze()

def solver(row, column):
    if  row < 0 or column < 0 or row == 5 or column == 5 or maze[row][column] == 2 or maze[row][column] == 1:
        return False

    if maze[row][column] == -1:
        return True
    maze[row][column] += 2
    print_maze()
    # TRY to move in every direction
    if solver(row, column + 1) == True: #right
        return True
    if solver(row, column - 1) == True:  # left
        return True
    if solver(row + 1, column) == True:  # down
        return True
    if solver(row - 1, column) == True:  # up
        return True
    return False
solver(0,0)
'''
maze[row][column] = 2
move_down()
#0, 1 ||  #1, 0
move_down()
#0, 2 || #2, 0
move_right()
#1, 2 || #2, 1
move_right()
#2, 2 || #2, 2
move_up()
#2, 1 || #1, 2
move_up()
#2, 0 || #0, 2
move_right()
#3, 0 || #0, 3
move_right()
#4, 0 || #0, 4
'''
