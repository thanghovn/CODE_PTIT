N = int(input())
A = list(map(int, input().split()))

# Để đảm bảo chọn giá trị xuất hiện đầu tiên khi có nhiều đáp án
# Ta sẽ duyệt theo thứ tự ban đầu của mảng

min_steps = float('inf')
best_value = -1

for i in range(N):
    target = A[i]
    steps = 0
    for x in A:
        steps += abs(x - target)

    # Cập nhật nếu tìm được cách tốt hơn
    # Hoặc bằng nhau nhưng target này xuất hiện sớm hơn (vì đang duyệt từ trái sang)
    if steps < min_steps or (steps == min_steps and (best_value == -1 or i < A.index(best_value))):
        min_steps = steps
        best_value = target

print(min_steps, best_value)