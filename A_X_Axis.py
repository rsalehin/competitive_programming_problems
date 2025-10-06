t = int(input().strip())
for _ in range(t):
    x1, x2, x3 = list(map(int, input().strip().split()))
    min_dist = 100000000
    min_ = min(x1, x2, x3)
    max_ = max(x1, x2, x3)
    for i in range(min_, max_+1):
        dist = abs(i -x1) + abs(i - x2) + abs(i - x3)
        min_dist = min(min_dist, dist)
    print(min_dist)