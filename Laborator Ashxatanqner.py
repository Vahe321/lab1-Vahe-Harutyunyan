
""""#(1----------------Verjavor avtomat---------------------------------)
n = input()


skizb = "q0"
verjnaka = "0"

for i in n:
    if skizb == "q0":
        if i == "0":
            skizb = "0"
        elif i == "1":
            skizb = "1"
    elif skizb == "q1":
        if i == "0":
            skizb = "q0"
        elif i == "1":
            skizb = "q1"
if skizb == verjnaka:
    print("tox@ yndunvac e ")
else:
    print("tox@ yndunvac che ")"""

#2-----------------DFS Grafner----------------------)
"""graph = {
    1: [2,3],
    2: [4,5],
    3: [7],
    4: [],
    5: [],
    6: [],
    7: [] 

}
visited = set()
def DFS(v):
    print(v, end=" ")
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            DFS(i)

DFS(1)"""
#3--------------------kapvac gagatner xmbavorum------------------
"""graph = {
    1: [2],
    2: [1],
    3: [],
    4: [4],
    5: [5],


}

visited = set()
def dfs(v,comp):
    print(v, end=" ")
    visited.add(v)
    comp.append(v)
    for i in graph[v]:
        if i not in visited:
            dfs(i,comp)
components = []

for v in graph:
    if v not in visited:
        c = []
        dfs(v, c)
        components.append(c)

print(components)"""
#4-------------------BFS graph--------------------
"""from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

visited = set()
q = deque([1])

while q:
    v = q.popleft()
    if v not in visited:
        print(v, end=" ")
        visited.add(v)
        for u in graph[v]:
            q.append(u) """

#5-------------BFS matrix-----------------
"""grid = [
    [1,1,0],
    [0,1,0],
    [1,1,1]
]

n, m = 3, 3
visited = [[False]*m for _ in range(n)]

from collections import deque

q = deque([(0,0)])
visited[0][0] = True

while q:
    x, y = q.popleft()
    print(x, y)
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))"""

#6-------------topologikakan sortavorum-----------
"""graph = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

visited = set()
order = []

def dfs(v):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(u)
    order.append(v)

for v in graph:
    if v not in visited:
        dfs(v)

print(order[::-1])"""
#7---------------deykotayin algoritm---------------
"""import heapq

graph = {
    1: [(2,1),(3,4)],
    2: [(3,2),(4,5)],
    3: [(4,1)],
    4: []
}

dist = {v: float('inf') for v in graph}
dist[1] = 0

pq = [(0,1)]

while pq:
    d, v = heapq.heappop(pq)
    for u, w in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            heapq.heappush(pq, (dist[u], u))

print(dist)"""

#8-------------gci hatum----------------------
"""def intersect(a,b,c,d):
    def orient(p,q,r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

    return orient(a,b,c)*orient(a,b,d) < 0 and orient(c,d,a)*orient(c,d,b) < 0

print(intersect((0,0),(4,4),(0,4),(4,0)))"""

#9-------------jarvis March-------------------
"""def jarvis(points):
    hull = []
    left = min(points)
    p = left
    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if (q == p) or ((r[0]-p[0])*(q[1]-p[1]) > (r[1]-p[1])*(q[0]-p[0])):
                q = r
        p = q
        if p == left:
            break
    return hull"""

#10----------------Graham Scan-----------------
"""def graham(points):
    points.sort()
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]"""

#11-------------Belman-Ford----------------
"""edges = [(1,2,4),(1,3,5),(2,3,-3)]
dist = {1:0,2:1e9,3:1e9}

for _ in range(2):
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

print(dist)"""

#12-------------Flod-Vashal-------------
"""INF = 10**9
dist = [
    [0, 3, INF],
    [INF, 0, 1],
    [2, INF, 0]
]

n = 3
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist)"""








