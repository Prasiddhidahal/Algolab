#importing
import time
import matplotlib.pyplot as plt
from itertools import permutations

# Backtracking helper functions
def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_backtracking(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_backtracking(board, col + 1, n): #Recursive function that tries to place queens column by column and backtracks if a column placement fails.
                return True
            board[i][col] = 0  
    return False

def n_queens_backtracking(n): #STARTS BACKTRACKING
    board = [[0] * n for _ in range(n)]
    if solve_n_queens_backtracking(board, 0, n):
        return board
    else:
        return None

# Brute force helper function
def is_valid_permutation(perm):
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(perm[i] - perm[j]) == j - i:
                return False
    return True

def n_queens_brute_force(n):
    columns = range(n)
    for perm in permutations(columns):
        if is_valid_permutation(perm):
            board = [[0] * n for _ in range(n)]
            for i in range(n):
                board[i][perm[i]] = 1
            return board
    return None

# Function to measure the time taken by each method
def measure_time(n, method):
    start_time = time.time()
    if method == 'backtracking':
        n_queens_backtracking(n)
    elif method == 'brute_force':
        n_queens_brute_force(n)
    end_time = time.time()
    return end_time - start_time

# List of board sizes
board_sizes = list(range(1, 11))  # From 1 to 10
backtracking_times = []
brute_force_times = []

# Measure time for each board size
for n in board_sizes:
    print(f"Measuring time for n={n}")
    backtracking_time = measure_time(n, 'backtracking')
    backtracking_times.append(backtracking_time)
    
    brute_force_time = measure_time(n, 'brute_force')
    brute_force_times.append(brute_force_time)
    
#x-size of board, y - tt
# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(board_sizes, backtracking_times, label='Backtracking', marker='o')
plt.plot(board_sizes, brute_force_times, label='Brute Force', marker='x')
plt.xlabel('Board Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Performance of N-Queens Solvers')
plt.legend()
plt.grid(True)
plt.show()


