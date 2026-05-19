def solve():
    s = list(input().strip())
    n = len(s)

    # Bước 1: Tìm vị trí i-1 từ phải sang trái
    i = n - 1
    while i > 0 and s[i - 1] <= s[i]:
        i -= 1

    # Bước 2: Nếu không tìm thấy
    if i == 0:
        print("-1")
        return

    # Vị trí cần đổi là i-1
    pos_to_change = i - 1

    # Bước 3: Tìm s[j] lớn nhất ở sau pos_to_change nhưng nhỏ hơn s[pos_to_change]
    best_j = i
    for j in range(i, n):
        if s[j] < s[pos_to_change]:
            if s[j] > s[best_j]:
                best_j = j

    # Xử lý trường hợp có nhiều chữ số giống nhau (như số 35441)
    # Ta chọn chữ số s[j] xuất hiện đầu tiên trong nhóm các chữ số giống nhau
    while best_j > 0 and s[best_j] == s[best_j - 1]:
        best_j -= 1

    # Đổi chỗ
    s[pos_to_change], s[best_j] = s[best_j], s[pos_to_change]

    # Bước 4: Kiểm tra số 0 ở đầu
    if s[0] == '0':
        print("-1")
    else:
        print("".join(s))


t = int(input())
for _ in range(t):
    solve()