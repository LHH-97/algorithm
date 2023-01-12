#BFS
from collections import deque

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
m = int(input())
graph = [ [] for i in range(n+1) ]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False]*(n+1)
bfs(graph,1,visited)

cnt = visited.count(True) - 1

print(cnt)

#DFS
def dfs(graph,v,visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph,i,visited)

n = int(input())
m = int(input())
graph = [ [] for i in range(n+1) ]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False]*(n+1)
dfs(graph,1,visited)

cnt = visited.count(True) - 1

print(cnt)