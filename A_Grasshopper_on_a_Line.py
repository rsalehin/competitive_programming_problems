t = int(input().strip())
for _ in range(t):
    x, k = list(map(int, input().strip().split()))
    if x%k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x-1, 1)