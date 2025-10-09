t = int(input().strip())
for _ in range(t):
    w, h, n = map(int, input().split())
    total = 1

    while w % 2 == 0:
        w //= 2
        total *= 2
    while h % 2 == 0:
        h //= 2
        total *= 2

    if total >= n:
        print("YES")
    else:
        print("NO")
