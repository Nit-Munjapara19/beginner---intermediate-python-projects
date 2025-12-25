import random

symbols = {1: "◼", 2: " ", 3: "◻"}

# create a 5x5 board with random symbols
board = [symbols[random.choice([1, 2, 3])] for _ in range(25)]

def print_board(board, size=5):
    for i in range(0, len(board), size):
        print(" ".join(board[i:i+size]))    

print_board(board)
