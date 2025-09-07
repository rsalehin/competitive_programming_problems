def solve():
    # string 2 of length 3
    n = int(input().strip())
    for _ in range(n):
        word = input().strip().lower()
        if word == 'yes':
            print('YES')
        else:
            print('NO')
solve()