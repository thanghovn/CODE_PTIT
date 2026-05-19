def prime (n) :
    if n < 2 :
        return False
    for i in range(2,int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

n, m = map(int, input().split())
matrix = []
for _ in range(n) :
    val = list(map(int, input().split()))
    matrix.append(val)

for i in range(n) :
    for j in range(m) :
        if prime(matrix[i][j]) :
            print(1, end=' ')
        else :
            print(0, end=' ')
    print()