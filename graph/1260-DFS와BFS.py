import sys
from collections import deque
sys.setrecursionlimit(10**9)
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

dcnt = 1
bcnt = 1

queue = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(r):
    global dcnt
    dfs_visited[r] = dcnt

    graph[r].sort()

    for g in graph[r]:
        if dfs_visited[g] == 0:
            dcnt += 1
            dfs(g)

def bfs(r):
    global bcnt
    bfs_visited[r] = bcnt
    queue.append(r)

    while queue:
        node = queue.popleft()
        graph[node].sort()

        for g in graph[node]:
            if bfs_visited[g] == 0:
                bcnt += 1
                bfs_visited[g] = bcnt
                queue.append(g)

dfs(v)
bfs(v)
print(' '.join(map(str, dfs_visited[1:])))
print(' '.join(map(str, bfs_visited[1:])))