t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    max_quality = -1
    winner = -1
    for i in range(n):
        length, quality = map(int, input().strip().split())
        if length <= 10 and quality > max_quality:
            max_quality = quality
            winner = i + 1
    print(winner)
        