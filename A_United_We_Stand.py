t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()
    
    # If all numbers are same, impossible
    if a[0] == a[-1]:
        print(-1)
        continue

    # Put all occurrences of smallest number into b
    b = [x for x in a if x == a[0]]
    c = [x for x in a if x != a[0]]
    
    print(len(b), len(c))
    print(*b)
    print(*c)
