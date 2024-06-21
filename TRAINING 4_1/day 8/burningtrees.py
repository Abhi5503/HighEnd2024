#one tree  is burnt and all the four corners of the trees are burnt which indicate 1 and empty land as 0...trees are
#only burnt in 4 ways and not diagonal..show the number of trees that are not burnt..!
def burningtrees(a, i, j, n):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return
    if a[i][j] == 1:
        a[i][j] = 2
    burningtrees(a, i - 1, j, n)
    burningtrees(a, i, j - 1, n)
    burningtrees(a, i + 1, j, n)
    burningtrees(a, i, j + 1, n)

def count_unburnt_trees(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                burningtrees(a, i, j, n)

    unburnt_count = sum(row.count(1) for row in a)
    return unburnt_count

a = [[0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0]]

unburnt_trees = count_unburnt_trees(a)
print("Number of unburnt trees:", unburnt_trees)
