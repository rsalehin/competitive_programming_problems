t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    directions = input().strip()
    x, y = 0, 0
    candy_position = (1, 1)
    was_there = False 
    for direction in directions:
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'L':
            x -= 1
        elif direction == 'R':
            x += 1

        if (x, y) == candy_position:
            was_there = True 
            break 

    if was_there:
        print('YES')
    else:
        print('NO')
