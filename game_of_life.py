import numpy as np

def initialize_grid(size):
    return np.random.choice([0, 1], size=(size, size))

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count live neighbors
            live_neighbors = np.sum(grid[max(0, i-1):min(i+2, grid.shape[0]), max(0, j-1):min(j+2, grid.shape[1])]) - grid[i, j]

            # Apply rules
            if grid[i, j] == 1:  # Alive cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = 0  
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[i, j] = 1  
    return new_grid

def print_grid(grid):
    """Display the grid."""
    for row in grid:
        print(" ".join(map(str, row)))

def game_of_life(size=15):
    grid = initialize_grid(size)

    while True:
        print("\nCurrent Generation:")
        print_grid(grid)

        user_input = input("Do you want to generate the next generation? (Y/N): ").strip().upper()
        if user_input == 'N':
            print("Game Over.")
            break
        elif user_input == 'Y':
            grid = update_grid(grid)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    game_of_life(size=15)
