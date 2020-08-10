# Author: Wil Coiner
# Date: 08/04/20
# Description: Can either play a game of Sudoku, solve a puzzle you enter, or have the program solve a random puzzle

import random, copy


class Sudoku:
    def __init__(self, puz):
        self.puzzle = list(puz)

    def set_cell(self, row, col, num):
        """Updates puzzle board"""
        self.puzzle[row][col] = num

    def sudoku_solver(self):
        """Solves puzzle"""
        # loop through every cell in puzzle
        curr = [0,0]
        # Base case. Check to see if puzzle is complete
        if self.check_empty(curr) is False:
            return True
        row = curr[0]
        col = curr[1]
        # Try values for cell
        for n in range(1, 10):
            # Check to see if number is available
            if self.check_row(curr, n) and self.check_column(curr, n) and self.check_subsquare(curr, n):
                self.puzzle[row][col] = n
                if self.sudoku_solver():
                    return True
            # Return cell to 0 for next attempt
            self.puzzle[row][col] = 0
        return False

    def check_empty(self, curr):
        """Checks if cell is empty"""
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    curr[0] = i
                    curr[1] = j
                    return True
        return False

    def check_subsquare(self, pos, n):
        """Checks if entry is available in subsquare"""
        row = pos[0] - pos[0] % 3
        col = pos[1] - pos[1] % 3
        curr = n
        for i in range(3):
            for j in range(3):
                if row + i == pos[0] and col + j == pos[1]:
                    continue
                elif self.puzzle[row + i][col + j] == curr:
                    return False
        return True

    def check_column(self, pos, n):
        """Checks if entry is available in column"""
        col = pos[1]
        curr = n
        for i in range(len(self.puzzle)):
            if i == pos[0]:
                continue
            elif self.puzzle[i][col] == curr:
                return False
        return True

    def check_row(self, pos, n):
        """Checks if entry is available in row"""
        row = pos[0]
        curr = n
        for i in range(len(self.puzzle)):
            if i == pos[1]:
                continue
            elif self.puzzle[row][i] == curr:
                return False
        return True

    def print_puzzle(self):
        """Prints current state of board"""
        # print boarder
        for j in range(len(self.puzzle)):
            print(j, end=" ")
            if (j + 1) % 3 == 0:
                print(" ", end=" ")
        print("")
        for j in range(len(self.puzzle)):
            print("-", end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print("")

        # print rows
        for i in range(len(self.puzzle)):
            # create subsquare border
            if (i + 1) % 3 == 0:
                for k in range(len(self.puzzle)):
                    print(self.puzzle[i][k], end=" ")
                    if (k + 1) % 3 == 0:
                        print("|", end=" ")
                print(i)
                for j in range(len(self.puzzle)):
                    print("-", end=" ")
                    if (j + 1) % 3 == 0:
                        print("|", end=" ")
                print("")
            else:
                for j in range(len(self.puzzle)):
                    print(self.puzzle[i][j], end=' ')
                    if (j + 1) % 3 == 0:
                        print("|", end=" ")
                print(i)
        print("\n")

    def solve_puzzle(self):
        """Initializes puzzle solve"""
        print("Puzzle:")
        self.print_puzzle()
        if self.sudoku_solver():
            print("Solution:")
            self.print_puzzle()
        else:
            self.print_puzzle()
            print("No solution")

    def verify_puzzle(self):
        """Verifies current state of puzzle is a valid solution"""
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                curr = [i, j]
                n = self.puzzle[i][j]
                if self.check_row(curr, n) and self.check_column(curr, n) and self.check_subsquare(curr, n):
                    continue
                else:
                    return False
        return True

def gameEngine(puzzle):
    og = copy.deepcopy(puzzle)
    p = Sudoku(puzzle)
    og_p = Sudoku(og)
    continue_game = True
    while continue_game is True:
        p.print_puzzle()
        num = input("Enter number (1-9), enter 'STOP' to quit the game and see the solution, or enter 'DONE' to check if puzzle is solved: ")
        if num == 'STOP':
            og_p.solve_puzzle()
            continue_game = False
        elif num == 'DONE':
            validate = p.verify_puzzle()
            if validate is True:
                p.print_puzzle()
                print("Congrats! You solved the puzzle!")
                continue_game = False
            else:
                print("This is not a solution")
        else:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            p.set_cell(row, col, int(num))



def main():
    puzzles = ([[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]],

            [[0, 0, 4, 0, 2, 0, 0, 3, 0],
            [5, 0, 0, 4, 0, 0, 0, 0, 0],
            [2, 8, 0, 0, 7, 0, 0, 0, 6],
            [0, 1, 7, 2, 0, 0, 0, 0, 0],
            [0, 9, 0, 1, 5, 6, 0, 4, 0],
            [0, 0, 0, 0, 0, 4, 1, 2, 0],
            [6, 0, 0, 0, 4, 0, 0, 5, 1],
            [0, 0, 0, 0, 0, 5, 0, 0, 8],
            [0, 2, 0, 0, 8, 0, 3, 0, 0]])

    playornot = input("Type '1' to play Sudoku. Type '2' to enter a Sudoku puzzle for the program to solve. Type '3' to have the program solve a random puzzle: ")
    if playornot == '1':
        num = random.randint(0,1)
        gameEngine(puzzles[num])
    elif playornot == '3':
        num = random.randint(0,1)
        p = Sudoku(puzzles[num])
        p.solve_puzzle()
    else:
        count_correct = False
        while count_correct is False:
            print("\n")
            print("Enter a 9x9 Sudoku puzzle by typing each cell separated by a comma, left to right, top to bottom.")
            puzzle = []
            for i in range(9):
                row = input("Enter '0' for an empty cell. Enter row " + str(i+1) + ": ")
                row = row.split(",")
                puzzle.append(row)
            count = 0
            for row in puzzle:
                for col in row:
                    count += 1
            if count == 81:
                for i in range(9):
                    for j in range(9):
                        puzzle[i][j] = int(puzzle[i][j])
                p = Sudoku(puzzle)
                p.solve_puzzle()
                count_correct = True
            else:
                print("Input not valid. Please try again.")


if __name__ == '__main__':
    main()

