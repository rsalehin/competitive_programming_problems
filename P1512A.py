def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        # Determine majority element using first three
        if arr[0] == arr[1]:
            majority = arr[0]
        else:
            majority = arr[2] if arr[2] == arr[0] or arr[2] == arr[1] else arr[0]
        
        # Find spy
        for i in range(n):
            if arr[i] != majority:
                print(i+1)  # 1-based index
                break
