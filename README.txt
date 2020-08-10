sudokuSolver README

This program can be used for 3 different tasks:
1. Play Sudoku (by inputting cell to insert a number 1-9)
2. Solve a puzzle that the user inputs
3. Solve a random puzzle

To run the program:
1. Navigate to file location via Terminal/Powershell and make sure the input file is in the same directory
2. Type “python3 sudokuSolver.py” via Terminal or “python sudokuSolver.py” via Powershell
3. Console will then print instructions along with input fields for the user to interact

To Play:
1. Type '1' in the console and hit enter
2. Console will print a random puzzle to solve
3. Enter a number 1-9 in which you'd like to enter in an empty cell
4. Enter the row you'd like insert the number
5. Enter the column you'd like to insert
6. Enter 'STOP' to quit the game and see the solution (the program runs a solver function along with subroutines to solve)
7. Enter 'DONE' to verify if current state of board solves the puzzle. Will either print that you have solved or have not

Enter a puzzle for program to solve:
1. Type '2' in the console and hit enter
2. Enter one row at a time each cell with a comma deliminating the next cell. Enter '0' for an empty cell
3. When you hit enter after the last row the program will run a solver function along with subroutines to solve
4. If incorrectly formatted input is provided program will tell you so and ask for input again

Solve Random Puzzle:
1. Type '3' in the console and hit enter
2. This will automatically print a puzzle then run a solver function to solve the puzzle
3. It will print the results of the puzzle if solvable