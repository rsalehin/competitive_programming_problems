def solve():
    k, r = map(int, input().split())
    buy = 1
    while True:
        total = k * buy
        if total % 10 == 0 or total % 10 == r:
            print(buy)
            return
        buy += 1
solve()