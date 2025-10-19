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
        # arr = list(map(int, input().split()))     
        # s = input().strip()  
        pile_A = 0
        total = sum([2**i for i in range(1, n+1)])
        for i in range(n//2, n):
            pile_A += 2**i
        pile_B = total - pile_A
        print(abs(pile_A-pile_B))                      
        


if __name__ == "__main__":
    main()