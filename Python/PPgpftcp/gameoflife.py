import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#x = np.array([[0,0,255],[255,255,0],[0,255,0]])
x = np.random.choice([0,255], 10*10, p=[0.2, 0.8]).reshape(10, 10)

N = 5

def addGlider(i, j, grid):
    """ads a glider with top left cell at i, j"""
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    grid[i:i+3, j:j+3] = glider
grid = np.zeros(N*N).reshape(N, N)
addGlider(1, 1, grid)

plt.imshow(x, interpolation='nearest')

plt.show()
