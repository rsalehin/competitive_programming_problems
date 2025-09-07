def solve():
    n = int(input().strip())
    pts = list(map(int, input().split()))
    left = 0
    right = len(pts) - 1
    sereja = True
    sereja_score = 0
    dima_score = 0
    while left <= right:
        if sereja:
            if pts[left] >= pts[right]:
                sereja_score += pts[left]
                left += 1 
                sereja = not sereja
            else:
                sereja_score += pts[right]
                right -= 1 
                sereja = not sereja
        else:
            if pts[left] >= pts[right]:
                dima_score += pts[left]
                left += 1 
                sereja = not sereja
            else:
                dima_score += pts[right]
                right -= 1 
                sereja = not sereja

    print(sereja_score, dima_score)
solve()