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
        n, m = list(map(int, input().split()))     
        # s = input().strip()
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(2*m)                        
        


if __name__ == "__main__":
    main()