def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve():
    n = int(input().strip())
    for i in range(4, n):
        j = n - i
        if not is_prime(i) and not is_prime(j):
            print(i, j)
            return
solve()