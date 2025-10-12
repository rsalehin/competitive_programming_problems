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
        # arr = list(map(int, input().split()))     
        # s = input().strip()    
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))                    
        current_gold = 0
        count = 0
        for gold in arr:
            if gold >= k:
                current_gold += gold 
            elif gold == 0:
                if current_gold >=1:
                    current_gold -= 1
                    count += 1
        print(count)


if __name__ == "__main__":
    main()