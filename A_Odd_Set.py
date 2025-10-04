t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    even = 0
    odd = 0
    arr = list(map(int, input().strip().split()))
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd:
        print("Yes")
    else:
        print("No")