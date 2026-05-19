def sosanh(a, b):
    # So sánh hai số dạng chuỗi
    if len(a) != len(b):
        return len(a) - len(b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

while True:
    try:
        N = int(input().strip())
        if N == 0:
            break
    except:
        break

    # Đọc N số (dạng chuỗi)
    numbers = []
    for _ in range(N):
        s = input().strip()
        # Loại bỏ các số 0 ở đầu (leading zeros), nhưng giữ lại nếu toàn bộ là 0
        s = s.lstrip('0')
        if not s:          # trường hợp số là 0 hoặc chỉ toàn 0
            s = '0'
        numbers.append(s)

    if not numbers:
        continue

    # Tìm min và max
    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers[1:]:
        if sosanh(num, min_num) < 0:
            min_num = num
        if sosanh(num, max_num) > 0:
            max_num = num

    # Kiểm tra tất cả có bằng nhau không
    if min_num == max_num:
        print("BANG NHAU")
    else:
        print(min_num, max_num)