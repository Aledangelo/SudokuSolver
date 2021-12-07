# SudokuSolver
Sudoku is a logic game where you want to insert the numbers from 1 to 9 in a 9x9 matrix, divided in turn into 9 sub-matrices (boxes) 3x3, where some numbers are already present in some elements of the matrix. Each row, column, and sub-array must contain each number only once. For the game to be valid, the numbers already present must ensure that there is one and only one solution.

![alt text](https://www.iltuocruciverba.com/wp-content/uploads/2014/02/sudoku-ragazzi-5-b.jpg)

* Some elements of the matrix already have digits
* A digit must be entered for each empty cell so that each row, column and sub-matrix contains each digit only once
* For the game to be valid, the numbers already present must ensure that there is only one solution

Solving the game means finding the only feasible solution (if any)

## Input Matrix
First I create a matrix in file .dat where I put a zero in correspondence of an empty box, and in the non-empty boxes I put the numbers. 

## Installation
* pip3 install -r requirements.txt
