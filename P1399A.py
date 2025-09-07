def solve():
    n = int(input().strip())
    for _ in range(n):
        length = int(input().strip())
        arr = list(map(int, input().split()))
        arr.sort()
        possible = True
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                possible = False
                break
        if possible:
            print("YES")
        else:
            print("NO")
solve()