from collections import deque

def bfs(graph,v,visited1):

    queue = deque([v])
    visited1[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited1[i]:
                queue.append(i)
                visited1[i] = True

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n,m,v = map(int,input().split())

graph = [[] for i in range(n+1)]
'''
graph = []

for _ in range(n+1):
    graph.append([])
'''

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,n+1):
    graph[i].sort()


visited = [False]*(n+1)
visited1 = [False]*(n+1)
dfs(graph,v,visited)
print()
bfs(graph,v,visited1)

#해당 문제에 대한 정리: https://keep-going99.tistory.com/427