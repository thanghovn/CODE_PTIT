def valid(n):
    if n != n[::-1] or len(n) % 2 != 0:
        return False
    for char in n:
        if int(char) % 2 != 0:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(2, n, 2):   # 👈 nhảy 2 bước, chỉ duyệt số chẵn
            if valid(str(i)):
                print(i, end=' ')
        print()

main()
