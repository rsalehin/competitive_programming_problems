def solve():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    groups = {1: [], 2: [], 3: []}
    
    for i, s in enumerate(arr):
        groups[s].append(i+1)
    
    team_count = min(len(groups[1]), len(groups[2]), len(groups[3]))
    
    print(team_count)
    for i in range(team_count):
        print(groups[1][i], groups[2][i], groups[3][i])
solve()