def solve():
    t = int(input().strip())
    for _ in range(t): 
        a, b = list(map(int, input().split()))
        print(b - a)
solve()