'''
ip : 5
 0 1 0 0 1
 1 0 0 1 1      1-land
 0 0 0 0 0      0-water
 1 0 0 0 0
 1 0 0 0 1
 
 op:5
'''
def numIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    def dfs(row, col):
        # Base cases for terminating the DFS
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
            return
        # Mark the current cell as visited by changing '1' to '0'
        grid[row][col] = '0'
        # Visit all 4 neighbors (up, down, left, right)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    island_count = 0
    
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Found a new island
                island_count += 1
                # Perform DFS to mark all connected '1's as visited
                dfs(i, j)
    
    return island_count


grid = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]


grid_str = [['1' if val == 1 else '0' for val in row] for row in grid]
num_islands = numIslands(grid_str)
print(num_islands) 

 