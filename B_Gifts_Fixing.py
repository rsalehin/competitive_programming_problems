t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    moves = 0
    for i in range(n):
        da = a[i] - min_a
        db = b[i] - min_b
        moves += max(da, db)
    print(moves)
