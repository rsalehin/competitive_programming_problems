def solve():
    a, b = list(map(int, input().split()))
    mixed = min(a, b)
    single = (max(a, b) - min(a, b)) // 2
    print(mixed, single)
solve()