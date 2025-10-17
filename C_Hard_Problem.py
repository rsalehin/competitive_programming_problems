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
        m, a, b, c = list(map(int, input().split()))     
        # s = input().strip()        
        result = 0
        
        if a >= m:
            result += m
        else:
            result += a 
            remaining = m - a 
            if c >= remaining:
                result += remaining 
                c -= remaining
            else:
                result += c
                c =0
        if b >= m:
            result += m       
        else:
            result += b 
            remaining = m - b 
            if c >= remaining:
                result += remaining 
                c -= remaining
            else:
                result += c
                c =0
        print(result)             
        


if __name__ == "__main__":
    main()