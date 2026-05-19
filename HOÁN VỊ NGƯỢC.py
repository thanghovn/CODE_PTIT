from itertools import permutations
from math import factorial

T = int(input())

for _ in range(T):
    n = int(input())

    a = list(range(n, 0, -1))

    print(factorial(n))

    for p in permutations(a):
        print(''.join(map(str, p)), end=' ')

    print()