import time
import os

# Grid size
SIZE = 41
grid = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

# Ant position and direction
x, y = SIZE // 2, SIZE // 2
# Directions: Up, Right, Down, Left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = 0  # Start facing Up

def print_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(row))

for _ in range(11000):
    print_grid()
    current = grid[x][y]

    # Turn and flip
    if current == '.':
        dir_index = (dir_index + 1) % 4  # Right
        grid[x][y] = '#'
    else:
        dir_index = (dir_index - 1) % 4  # Left
        grid[x][y] = '.'

    # Move forward
    dx, dy = directions[dir_index]
    x += dx
    y += dy

    # Boundary check
    if not (0 <= x < SIZE and 0 <= y < SIZE):
        break

    time.sleep(0.01)
