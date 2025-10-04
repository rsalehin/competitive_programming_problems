t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = input().strip()
    empty_cells = 0
    contiguous = 1
    for i in range(n):
        if arr[i] == '.':
            empty_cells += 1
            if i > 0 and arr[i - 1] == '.':
                contiguous += 1
                if contiguous >=3:
                    break
            else:
                contiguous = 1 
    if contiguous >= 3:
        print(2)
    else:
        print(empty_cells)