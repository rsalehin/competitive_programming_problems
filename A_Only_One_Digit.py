t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    digits = []
    while x>0:
        digit = x % 10
        digits.append(digit)
        x = x//10
    digits.sort()
    print(digits[0])