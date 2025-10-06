t = int(input().strip())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(m):
            if arr_n[i] + arr_m[j] <=k:
                count += 1
    print(count)