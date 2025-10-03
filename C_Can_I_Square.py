import math

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    buckets = map(int, input().split())
    total = 0
    for bucket in buckets:
        total += bucket 
    root = math.isqrt(total)
    if root * root == total:
        print('YES')
    else:
        print('NO')