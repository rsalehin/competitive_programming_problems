t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % 2 == 1:
        print("YES")
    elif any(a % 2 == 0 for a in arr) and any(a % 2 == 1 for a in arr):
        print("YES")
    else:
        print("NO")
