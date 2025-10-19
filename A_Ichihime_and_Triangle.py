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
        a, b, c, d = list(map(int, input().split()))     
        # s = input().strip()            
        x, y, z = b, c, c 
        print(x, y, z)            
        


if __name__ == "__main__":
    main()