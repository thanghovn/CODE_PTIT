import sys
sys.setrecursionlimit(100000)

def dfs(u, banned, adj, visited):
    visited[u] = True
    for v in adj[u]:
        if v != banned and not visited[v]:
            dfs(v, banned, adj, visited)

def count_components(n, adj, banned):
    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if i == banned:
            continue
        if not visited[i]:
            cnt += 1
            dfs(i, banned, adj, visited)

    return cnt

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    original = count_components(n, adj, 0)

    best = original
    ans = 0

    for i in range(1, n + 1):
        after = count_components(n, adj, i)

        if after > best:
            best = after
            ans = i

    print(ans)