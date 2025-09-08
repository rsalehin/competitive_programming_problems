def solve():
    t = int(input().strip())
    for _ in range(t):
        word = input().strip()
        if word[0] == 'a' or word[1] == 'b' or word[2] == 'c':
            print('YES')
        else:
            print('NO')
solve()