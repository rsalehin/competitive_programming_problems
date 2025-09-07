def solve():
    n = int(input().strip())
    for _ in range(n):
        k, x = list(map(int, input().split()))
        for _ in range(k):
            if x % 2 == 1:
                x = (x-1)//3
            else:
                x *= 2
        print(x)
solve()