import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = True
    adj[v][u] = True

# Gọi x[i] = 0/1: đỉnh i có bị chọn lẻ số lần hay không
# Chọn x[1] = 0
x = [0] * (n + 1)

for i in range(2, n + 1):
    if adj[1][i]:
        x[i] = 0      # có cạnh thì sau cùng cần cùng trạng thái
    else:
        x[i] = 1      # không có cạnh thì cần khác trạng thái

ok = True

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if adj[i][j]:
            # Nếu ban đầu có cạnh, sau các thao tác vẫn phải thành có cạnh
            # nên x[i] và x[j] phải giống nhau
            if x[i] ^ x[j] != 0:
                ok = False
                break
        else:
            # Nếu ban đầu không có cạnh, muốn thành có cạnh
            # thì phải đảo đúng 1 trong 2 đỉnh
            if x[i] ^ x[j] != 1:
                ok = False
                break

    if not ok:
        break

print("YES" if ok else "NO")
