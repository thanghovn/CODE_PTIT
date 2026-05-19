def hanoi(n, A, B, C):
    if n == 1:
        print(f"{A} -> {C}")
        return
    hanoi(n-1, A, C, B)
    print(f"{A} -> {C}")
    hanoi(n-1, B, A, C)

n = int(input())
hanoi(n, 'A', 'B', 'C')
