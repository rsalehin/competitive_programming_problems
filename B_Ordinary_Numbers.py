def is_ordinary(num):
    digits = set(str(num))
    return len(digits) == 1 
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    count = 0
    for i in range(1, n+1):
        if is_ordinary(i):
            count += 1
    print(count)
        
        
