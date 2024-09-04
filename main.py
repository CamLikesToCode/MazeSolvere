import time
import timeit

import Mazegenerator
from colorama import Fore, Style, init


maze_gen = Mazegenerator.MazeGenerator(20, 20)
maze = maze_gen.generate_maze(0,0)

def print_maze():
    for row in maze:
        for index in row:
            if index == 1:
                print(Fore.RED + "|", end =" ")
            if index == 0:
                print(Fore.LIGHTCYAN_EX + " ", end =" ")
            if index == 2:
                print(Fore.GREEN + "2", end =" ")
            if index == 3:
                print(Fore.YELLOW + "3", end=" ")
            if index == "x":
                print(Fore.RED + "x", end=" ")
        print()
        print()
    print(Fore.BLACK + "_______________________________________________")
    print()

generate = input("Enter anything to generate a maze: ")
print_maze()
solve = input(Fore.BLACK + "Enter anything to solve the maze: ")
column = 0 # x
row = 0 # y
'''
def move_up():
    global row
    row -= 1
    maze[row][column] = 2
    time.sleep(5)
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
'''
def solver(row, column):
    if  row < 0 or column < 0 or row == len(maze) or column == len(maze[0]) or maze[row][column] == 2 or maze[row][column] == 1:

        return False


    if maze[row][column] == 3:
        print(Fore.BLACK + "Finished")
        return True
    maze[row][column] += 2
    time.sleep(.1)
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

    maze[row][column] = "x"
    return False
solver(0,0)