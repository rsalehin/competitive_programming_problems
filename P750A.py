def solve():
    n, k = list(map(int, input().split()))
    finish_time = 4*60-k
    total = 0
    problem = 0
    for i in range(1, n+1):
        total += i*5
        if total <= finish_time:
            problem += 1
        if total > finish_time:
            break 
    print(problem)
solve()
