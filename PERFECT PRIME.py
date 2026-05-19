def dao(n) :
    return int(n[::-1])
def to_prime(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    num  = int(input())
    if to_prime(num) and to_prime(dao(str(num))):
        print('Yes')
    else :
        print('No')