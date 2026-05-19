from collections import deque

n, m, x = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

# BFS từ đỉnh X để tìm thành phần liên thông chứa X
q = deque([x])
visited[x] = True

while q:
    u = q.popleft()

    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

# Các đỉnh không cùng thành phần liên thông với X
ans = []

for i in range(1, n + 1):
    if not visited[i]:
        ans.append(i)

if len(ans) == 0:
    print(0)
else:
    for v in ans:
        print(v)