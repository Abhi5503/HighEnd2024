'''
d = {5:[7,3],3:[5,7,8],7:[5,4],4:[2,7,8],8:[2,3,4],2:[4,8]}
print("BFS:")
visited = set()
q = []
for i in d:
    if i not in visited:
        visited.add(i)
        q.append(i)
    while(q):
        node = q.pop(0)
        print(node,end=" ")
        for n in d[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)
print("\nVisited:",visited)
'''
'''
d = {5:[7,3],7:[4,5],4:[7,6],3:[5,8],8:[2,3],6:[4],2:[8]}
vi = []
q = []
for i in d:
    if i not in vi:
        vi.append(i)
        q.append(i)
    while(q):
        n = q.pop(0)
        print(n,end=" ")
        for i in d[n]:
            if i not in vi:
                vi.append(i)
                q.append(i)
if (q==[]):
    print(True)
else:
    print(False)
'''

'''
#dijkstra's algo(shortest path algorithm)
g = {
    5: [(7, 2), (3, 3)], 
    3: [(5, 3), (7, 5), (8, 6)], 
    7: [(5, 2), (4, 8)], 
    4: [(2, 1), (7, 8), (8, 4)], 
    8: [(2, 7), (3, 6), (4, 4)], 
    2: [(4, 1), (8, 7)]
}

def dijkstras(g, src):
    d = {5: 9999, 3: 9999,7:9999, 4: 9999, 8: 9999, 2: 9999}
    d[src] = 0
    visited = set()
    q = [src]

    while q:
        node = q.pop(0)
        for nbr,wt in g[node]:
            if nbr not in visited:
                if d[nbr] > d[node] + wt:
                    d[nbr] = d[node] + wt
                    q.append(nbr)
        visited.add(node)
    return d
print(dijkstras(g, 5))
'''


    
    

