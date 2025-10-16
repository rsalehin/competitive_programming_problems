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
        size = 2 * n
        for r in range(size):
            for c in range(size):
                block_row = r // 2
                block_column = c // 2
                if (block_row + block_column)%2 == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            print()                    
        


if __name__ == "__main__":
    main()