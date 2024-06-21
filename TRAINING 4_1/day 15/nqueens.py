def nqueens(row):
    if(row==n):
        return
    for col in range(n):
        if(check(row,col)):
            grid[row][col]=1
            return nqueens(row+1)
            
def check(i,j):
    if(i==u):
        return 0
    elif(j==v):
        return 0
    row = i,col = j
    for i in range(j):
        if(grid[i][j]==1):
            return 0
    while(i>=0 and j>=0):
        if(grid[i][j]==1):
            return 0
        i=j-1
        j=j-1
    while():
        if(grid[row][col]==1):
            return 0
        r=r-1
        c=c+1
                       
n = int(input())
u,v = 2,3
grid = [[0]*n]*n
print(grid)
nqueens(0)