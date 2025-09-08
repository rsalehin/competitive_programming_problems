def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    y, w = map(int, input().split())
    m = max(y, w)
    num = 6 - m + 1
    den = 6
    g = gcd(num, den)
    print(f"{num // g}/{den // g}")

solve()