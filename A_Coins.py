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
        n, k = list(map(int, input().split()))     
        # s = input().strip()        
        if n == 1 and k == 1:
            print('YES')
            continue
        elif n==1 and k > 1:
            print('NO')
            continue
        
        if n%2 == 0:
            print('YES')
        else:
            if k%2 == 0:
                print('NO')
            else:
                print('YES')
                
                        
        


if __name__ == "__main__":
    main()