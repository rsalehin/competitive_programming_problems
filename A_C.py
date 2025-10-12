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
        # n = int(input().strip())                  
        a, b, n = list(map(int, input().split()))     
        # s = input().strip()
        count = 0
        while max(a, b) <= n:
            if a < b:
                a += b
            else:
                b += a
            count += 1
        print(count)
                                
        


if __name__ == "__main__":
    main()