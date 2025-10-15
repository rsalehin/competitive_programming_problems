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
        n = int(input().strip())                  
        arr = list(map(int, input().split()))     
        # s = input().strip()    
        total_prod = 1
        for num in arr:
            total_prod *= num
        current_prod = 1
        k = -1
        for i, num in enumerate(arr):
            current_prod *= num
            complement = total_prod / current_prod
            if current_prod == complement:
                k = i + 1
                break
        print(k)                    
        


if __name__ == "__main__":
    main()