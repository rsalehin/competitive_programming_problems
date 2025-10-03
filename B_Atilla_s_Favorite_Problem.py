t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    max_ = -1
    text = input().strip()
    for ch in text:
        max_ = max(max_, ord(ch)-ord('a') + 1)
    print(max_)