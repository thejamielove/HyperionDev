def count_mines(grid):
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Define the directions to check for adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Create a new grid to store the mine counts
    result = [[0] * cols for _ in range(rows)]

    # Iterate over each cell in the grid
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            # Check if the current cell is a mine or empty
            if cell == "-":
                # Initialize a count variable to track the number of adjacent mines
                count = 0
                # Iterate over each direction to check adjacent cells
                for row_check, col_check in directions:
                    # Calculate the position of the adjacent cell
                    new_row = row_index + row_check
                    new_col = col_index + col_check
                    # Check if the adjacent cell is within the grid bounds and is a mine
                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == "#"
                    ):
                        # Increment the count if the adjacent cell is a mine
                        count += 1
                # Store the count in the corresponding cell of the result grid
                result[row_index][col_index] = str(count)
            else:
                # If the current cell is a mine, simply copy it to the result grid
                result[row_index][col_index] = "#"

    # Return the resulting grid with mine counts
    return result

# Grid to use count_mines function
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = count_mines(grid)
for row in result:
    print(row)