t = int(input().strip())
for _ in range(t):
    name = input().split(' ')
    modern_name = name[0][0] + name[1][0] + name[2][0]
    print(modern_name)