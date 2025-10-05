import math
t = int(input().strip())
for _ in range(t):
    a, b = list(map(int, input().strip().split()))
    c, d = list(map(int, input().strip().split()))
    e, f = list(map(int, input().strip().split()))
    g, h = list(map(int, input().strip().split()))
    side_one = math.sqrt((a-c)**2 + (b-d)**2)
    side_two = math.sqrt((a-e)**2 + (b-f)**2)
    if side_one == side_two:
        print(int(side_one * side_one))
    else:
        print(int(min(side_one, side_two)* min(side_one, side_two)))
    