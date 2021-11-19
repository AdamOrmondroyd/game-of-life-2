"""
Game of Life (goy) for RSE course with James Fergusson
"""

import numpy as np
from scipy.signal import convolve2d

BLINKER = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
GLIDER = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]])
BEACON_1 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]])
BEACON_2 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]])
                    
GOY_MASK = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

def step(cells):
    """
    Evolve cells one time step
    """
    
    # Count neighbours using convolution
    count = convolve2d(cells, GOY_MASK, mode='same', boundary='wrap')
    
    newcells = np.where(cells==1,np.where((count>1),np.where(count<4,1,0),0),np.where(count==3,1,0))
    
    return newcells

def run(start_cells, num_steps):
    """Advances start_cells by num steps and returns the result"""
    result = start_cells
    for i in range(num_steps):
        result = step(result)
    return result

def run_list(start_cells, num_steps):
    """Create list of arrays of game of life steps starting from start_cells"""
    result = []
    result.append(start_cells)
    next_cells = start_cells
    for i in range(num_steps):
        next_cells = step(next_cells)
        result.append(next_cells)
        
    return result

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter

    # stolen from solutions

    def animate(frame):
        """
        Animation function. Takes the current frame number (to select the potion of
        data to plot) and a line object to update.
        """
        # We have to use global variables here as animate can only take 'frame' which
        # is the frame number and not any other arguments
        global image, data

        # turn array into image
        image.set_array(data[frame])

        return image

    # Initialise
    cells = np.array([[0,0,0,0,0],
                      [0,0,0,1,0],
                      [0,1,0,1,0],
                      [0,0,1,1,0],
                      [0,0,0,0,0]])
    frames = 100

    # create list of arrays
    data = run_list(cells,frames)


    # Create plot
    fig, ax = plt.subplots(1, figsize=(1, 1))
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis("off")

    # Create image object
    image = ax.imshow(data[0], vmin=0, vmax=1)

    # Turn list of arrays into animation
    animation = FuncAnimation(fig,animate,np.arange(frames),fargs=[],interval=100)
    writergif = PillowWriter(fps=60)
    animation.save('my_glider.gif', writer=writergif)
   