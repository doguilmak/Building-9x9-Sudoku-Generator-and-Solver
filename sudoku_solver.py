# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:17:37 2022

@author: doguilmak

"""
#%%
# Building grid for Sudoku

import random 
"""
grid = [
        [7, 0, 2, 0, 5, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 9, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 4, 3, 0, 0, 0, 7, 5, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 9, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 4, 0, 2, 0, 3]    
    ]
"""

maxAttemp = 100 # Stops the program after 100 attempts
count = 9999
solveCounter = 0

while count > maxAttemp:
    solveCounter += 1
    puzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(0)
        puzzle.append(row)

    for row in range(9):
        for col in range(9):
            thisRow=puzzle[row]
            thisCol=[]
            for h in range(9):
                 thisCol.append(puzzle[h][col])

            subCol = int(col/3)
            subRow = int(row/3)
            subMat = []
            for subR in range (3):
                for subC in range (3):
                    subMat.append(puzzle[subRow * 3 + subR][subCol * 3 + subC])
            randVal = 0
            count = 0
            while randVal in thisRow or randVal in thisCol or randVal in subMat:
                randVal = random.randint(1, 9)
                count+=1

                if count > maxAttemp: break 
            puzzle[row][col] = randVal

            if count > maxAttemp: break 
        if count > maxAttemp:
            break

print('\nGrid generated:')
for r in puzzle:
    print(r)

print('\n')   

#%%
# Make grid with zeros

print('Make grid with zeros:')

# Determine number of zeros.
zero_num = 50

while zero_num>=0:
    n = random.randint(0, 8)
    m = random.randint(0, 8)
    if puzzle[n][m] != 0:
        puzzle[n][m] = 0
        zero_num -=1
    else:
        pass
    
grid=[]   
for r in puzzle:
    grid.append(r)
    print(r)
    

#Number of zeros in grid
import numpy as np
ZEROS = 80 - np.count_nonzero(grid)

print(f'\nIn grid, there are {ZEROS} zeros.\n')
   
#%%    
# Solving generated grid

print('\nSolving generated grid:')
M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end = " ")
        print('')
        
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):    
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
        
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    
    for num in range(1, M + 1, 1):     
        if solve(grid, row, col, num):         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist.")
