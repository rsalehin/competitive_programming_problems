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
        x, y, z = list(map(int, input().split()))     
        # s = input().strip()        
        r = max(x, y, z)
        s = min(x, y, z)
        count = [x, y, z].count(r)
        if count < 2:
            print('NO')
        else:
            print('YES')  
            print(r, s, r)              
        


if __name__ == "__main__":
    main()