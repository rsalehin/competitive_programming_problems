import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

# Fast input reading
input = sys.stdin.readline

# ========== MAIN ==========
def main():
    t = int(input().strip())
    for _ in range(t):
        n = input().strip()                 
        # arr = list(map(int, input().split()))     
        # s = input().strip()                        
        if len(n) < 3 or not n.startswith('10') :
            print('NO')
            continue
        exponent = n[2:]
        if len(exponent) > 1 and exponent.startswith('0'):
            print('NO')
            continue
        exponent_value = int(exponent) if exponent else 0
        if exponent_value >=2:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main()