t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()
    
    if s in x:
        print(0)
        continue
    
    found = False
    for ops in range(1, 10):
        x = x + x
        if s in x:
            print(ops)
            found = True
            break
    
    if not found:
        print(-1)
