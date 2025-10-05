t = int(input().strip())
for _ in range(t):
    q_row = -1
    for i in range(3):
        row = list(input())
        if '?' in row:
            q_row = i
            content = ['A', 'B', 'C']
            absent = [x for x in content if x not in row]
            print("".join(absent))
    