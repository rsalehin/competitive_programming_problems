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
        cnt = Counter(arr)
        if len(cnt) == 1:
            print('Yes')
            continue
        if len(cnt) > 2:
            print('No')
            continue
        
        counts = sorted(cnt.values())
        odd = (n+1) // 2
        even = n // 2
        if counts == sorted([odd, even]):
            print('Yes')
        else:
            print('No')                          
        


if __name__ == "__main__":
    main()