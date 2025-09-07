def solve():
    n = int(input().strip())
    for _ in range(n):
        division = int(input().strip())
        if division <= 1399:
            print('Division 4')
        elif 1400 <= division <=1599:
            print('Division 3')
        elif 1600 <= division <= 1899:
            print('Division 2')
        else:
            print('Division 1')
solve()