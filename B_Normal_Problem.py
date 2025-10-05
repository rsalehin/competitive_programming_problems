t = int(input().strip())
for _ in range(t):
    a = input().strip()
    b = ""
    for ch in a:
        if ch == 'p':
            b += 'q'
        elif ch == 'q':
            b += 'p'
        elif ch == 'w':
            b += 'w'
    print(b[::-1])