import math
t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    a = x - 1
    b = 1
    found = False
    while not found and a >0:
        if math.gcd(a, b) + math.lcm(a, b) == x:
            print(a, b)
            found = True 
        else:
            a -= 1
            b += 1