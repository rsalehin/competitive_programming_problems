t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    left = 0
    right = n - 1
    result = []
    while left <= right:
        result.append(str(arr[left]))
        left += 1
        if left > right:
            break
            
        result.append(str(arr[right]))
        right -= 1
        if left > right:
            break
    print(" ".join(result))