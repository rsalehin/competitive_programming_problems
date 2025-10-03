t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    result = []
    for i in range(n):
        row = input().strip()
        for j in range(4):
            if row[j] != '.':
                result.insert(0, str(j+1))
    print(" ".join(result))