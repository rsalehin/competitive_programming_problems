import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().split()))
    a = [b[0]]
    for i in range(1, n):
        a.append(b[i])
        if b[i] < b[i-1]:
            a.append(b[i])
    print(len(a))
    print(*a)
