from collections import defaultdict

def dfs(u, target, graph, visited, removed):
    if u == removed:
        return False
    if u == target:
        return True
    visited[u] = True

    for v in graph[u]:
        if not visited[v] and v != removed:
            if dfs(v, target, graph, visited, removed):
                return True
    return False


t = int(input())
for _ in range(t):
    n, m, u ,v = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a ,b = map(int, input().split())
        graph[a].append(b)

    count = 0
    for x in range(1,n+1):
        if x == u or x == v:
            continue

        visited = [False] * (n+1)
        if not dfs(u, v, graph, visited, x):
            count += 1

    print(count)