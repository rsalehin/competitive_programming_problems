t= int(input().strip())
for _ in range(t):
    n = int(input().strip())
    bags = list(map(int, input().strip().split()))
    mihai = 0
    bianca = 0
    for bag in bags:
        if bag%2==0:
            mihai += bag
        else:
            bianca += bag 
    if mihai > bianca:
        print('YES')
    else:
        print('NO')
            