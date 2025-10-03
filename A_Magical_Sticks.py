t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    total = 1
    if n <= 2:
        print(total)
    else:
        left = 1
        right = n-1 
        while left < right:
            if left + right == n:
                total += 1 
            left += 1
            right -= 1
        print(total)
    