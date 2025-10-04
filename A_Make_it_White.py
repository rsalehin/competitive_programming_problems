t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = input().strip()
    w_list = [i for i in range(n) if arr[i] == 'B']
    if not w_list:
        print(0)
    else:
        print(w_list[-1] - w_list[0]+1)