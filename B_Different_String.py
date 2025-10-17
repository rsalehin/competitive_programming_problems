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
        s = input().strip()
        freq = Counter(s)
        if len(freq) == 1:
            print('NO')
        else:
            print('YES')  
            print(s[1:]+s[0])                      
        


if __name__ == "__main__":
    main()