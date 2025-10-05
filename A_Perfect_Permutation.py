n = int(input().strip())

if n % 2 == 1:
    print(-1)
else:
    res = []
    for i in range(1, n+1, 2):
        res.append(i+1)
        res.append(i)
    print(*res)
