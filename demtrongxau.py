def main():
    for t in range(int(input())):
        s = input()
        n = input()
        id, cnt = s.find(n), 0
        while id != -1:
            cnt += 1
            id = s.find(n, id + len(n))
        print(cnt)
main()