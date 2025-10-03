t = int(input().strip())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    if 2*a < b:
        print(n * a)
    else:
        print((n // 2) * b + (n % 2) * a)
        
