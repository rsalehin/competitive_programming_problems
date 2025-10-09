t = int(input().strip())
for i in range(t): 
    w, h, n = list(map(int, input().split()))
    total = 1
    while ((w%2 == 0) or (h%2 == 0)):
        if w%2 == 0:
            w = w/2
            total += 1
        elif h%2 == 0:
            h = h/2
            total += 1
    print(total)