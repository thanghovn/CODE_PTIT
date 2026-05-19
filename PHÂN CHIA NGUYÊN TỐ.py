import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))

b = []
seen = set()
for num in a:
    if num not in seen:
        b.append(num)
        seen.add(num)
m = len(b)
total_sum = sum(b)
left_sum = 0

found = False
for i in range(m-1):
    left_sum += b[i]
    right_sum = total_sum - left_sum

    if is_prime(right_sum) and is_prime(left_sum):
        print(i)
        found = True
        break

if not found:
    print("NOT FOUND")