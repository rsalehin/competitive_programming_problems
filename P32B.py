def solve():
    code = input().strip()
    result = []
    i = 0
    while i < len(code):
        if code[i] == '.':
            result.append('0')
            i += 1
        else:  # must be '-'
            if code[i+1] == '.':
                result.append('1')
            else:  # code[i+1] == '-'
                result.append('2')
            i += 2
    print("".join(result))
solve()