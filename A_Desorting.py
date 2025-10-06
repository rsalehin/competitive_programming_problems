t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # check if already not sorted
    not_sorted = any(a[i] > a[i+1] for i in range(n-1))
    if not_sorted:
        print(0)
        continue

    # compute min operations
    min_ops = float('inf')
    for i in range(n-1):
        diff = a[i+1] - a[i]
        min_ops = min(min_ops, diff // 2 + 1)

    print(min_ops)
