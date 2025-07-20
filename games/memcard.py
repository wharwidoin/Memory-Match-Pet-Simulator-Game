import random

# Define a function to generate a grid with matching pairs
def generate_grid(rows, cols):
    num_pairs = (rows * cols) // 2
    symbols = [chr(ord('A') + i) for i in range(num_pairs)] * 2
    random.shuffle(symbols)
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(symbols.pop())
        grid.append(row)
    return grid

# Define a function to display the grid (with hidden and revealed cards)
def display_grid(grid, revealed):
    for i in range(len(grid)):
        row_display = []
        for j in range(len(grid[i])):
            if revealed[i][j]:
                row_display.append(grid[i][j])
            else:
                row_display.append('*')
        print(' '.join(row_display))
    print()

# Handle player input
def handle_input(rows, cols, prompt):
    while True:
        try:
            row, col = map(int, input(prompt).split())
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid input. Please enter values within grid bounds.")
        except ValueError:
            print("Invalid input. Format: row col (e.g. 0 1)")

# Check if all cards are revealed
def is_game_over(revealed):
    return all(all(row) for row in revealed)

# Play the memory game
def play_game(rows, cols):
    grid = generate_grid(rows, cols)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    attempts = 0

    while not is_game_over(revealed):
        display_grid(grid, revealed)
        print("Select the first card:")
        r1, c1 = handle_input(rows, cols, "Row Col: ")
        if revealed[r1][c1]:
            print("Card already revealed. Choose another.")
            continue

        revealed[r1][c1] = True
        display_grid(grid, revealed)

        print("Select the second card:")
        r2, c2 = handle_input(rows, cols, "Row Col: ")
        if revealed[r2][c2]:
            print("Card already revealed. Choose another.")
            revealed[r1][c1] = False
            continue

        revealed[r2][c2] = True
        display_grid(grid, revealed)

        if grid[r1][c1] != grid[r2][c2]:
            print("Not a match.")
            revealed[r1][c1] = False
            revealed[r2][c2] = False
        else:
            print("Match found!")
        attempts += 1

    print(f"Congratulations! You completed the game in {attempts} attempts.")

# Start the game (e.g. 2x4 grid)
if __name__ == "__main__":
    play_game(3, 4)
