# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 23:23:29 2021

@author: Serkan
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# from matplotlib import cm
import numpy as np
import msvcrt

bnw = ListedColormap([[1,1,1] , [0,0,0]]) # Define black and white for matshow
nrows, ncols = 41,41 # grid size
check = [1,-1,nrows-1,nrows,nrows+1,-nrows-1,-nrows,-nrows+1,] # Neighbour cell coordinates

def creategrid(): # Create the grid
    grid = np.zeros(nrows*ncols).reshape((nrows,ncols))
    grid[12:15,11] = 1  # Initial shape
    grid[13,13] = 1
    alive = [] # Array holding the locations of live cells
    for i in range(nrows*ncols): 
        if (grid.flatten().tolist()[i] != 0): # check if a cell is alive
            alive.append(i)
    return grid,alive
grid,alive = creategrid()

def life(): # Calculates who lives and dies
    alive_neigh_all = np.zeros(nrows*ncols)
    
    for i in range(nrows*ncols):
        for j in range(len(check)): # Check 8 neighbours 
            if (i+check[j] >= 0 and i+check[j] <=nrows*ncols-1): 
                if (grid.flatten().tolist()[i+check[j]] == 1):
                    alive_neigh_all[i] += 1 # add one for each alive neigh
                    
    dying_cells, borning_cells = [], []
    gridl = grid.flatten().tolist() 
    bornables = np.zeros(nrows*ncols).reshape((nrows,ncols)).flatten().tolist()
    
    for i in range(len(alive)): # Check if the alive cells will die
        if (alive_neigh_all[alive[i]] <2 or alive_neigh_all[alive[i]] >3): # Die condition
            dying_cells.append(alive[i])
            
    for i in range(nrows*ncols): # Check if the dead cells will born
        if (gridl[i] !=1):
            for j in range(len(check)): # Check all 8 neighbours 
                if (i+check[j] >= 0 and i+check[j] <=nrows*ncols-1):
                    if (gridl[i+check[j]] == 1) :
                         bornables[i] += 1 # add one for each alive neigh
        if (bornables[i] >= 3): # Born condition
            borning_cells.append(i)
    return(alive_neigh_all,borning_cells, dying_cells)

def plot_grid():
    golgrid = plt.matshow(grid, cmap = bnw)
    plt.show()
plot_grid()

def executer():
    alive_neigh, dying_cells, borning_cells = [], [], [] # Reset the lists
    [alive_neigh, borning_cells, dying_cells] = life()
    grid_new = np.array(grid.flatten().tolist()) # Create new grid
    for i in range(len(dying_cells)):
        grid_new[dying_cells[i]] = 0 # Kills the cell if it has less than 2 alive neighs
    for i in range(len(borning_cells)):
        grid_new[borning_cells[i]] = 1 # Borns the cell if it has more than 3 alive neighs
    grid_new = grid_new.reshape((nrows,ncols))
    alive_new = [] #locations of live cells
    for i in range(nrows*ncols): 
        if (grid_new.flatten().tolist()[i] != 0):
            alive_new.append(i)
    return(grid_new,alive_new)

for i in range(200):    
    grid,alive = executer()
    plot_grid()
    if (sum(sum(grid))<1):
        display('Life is over')
        break
    else:
        inp = input("input s to stop")
    if inp == 's':
        break