import numpy as np

def initialize_grid(size):
    return np.random.choice([0, 1], size=(size, size))

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            live_neighbors = np.sum(grid[max(0, i-1):min(i+2, grid.shape[0]), max(0, j-1):min(j+2, grid.shape[1])]) - grid[i, j]

            if grid[i, j] == 1: 
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = 0  
            else:  
                if live_neighbors == 3:
                    new_grid[i, j] = 1  
    return new_grid

def print_grid(grid):
    for row in grid:
        print(" ".join('■' if cell else ' ' for cell in row))

def game_of_life():
    while True:
        try:
            size = int(input("Enter the size of the grid (e.g., 15 for a 15x15 grid): "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            generations = int(input("Enter the number of generations to simulate: "))
            if generations > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    grid = initialize_grid(size)

    while True:
        for generation in range(generations):
            print(f"\nGeneration {generation + 1}:")
            print_grid(grid)
            grid = update_grid(grid)

        print("Simulation complete.")

        try:
            continue_gen = int(input("Enter the number of generations to simulate (or 0 to stop): "))
            if continue_gen == 0:
                print("Ending simulation.")
                break
            else:
                generations = continue_gen
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game_of_life()
