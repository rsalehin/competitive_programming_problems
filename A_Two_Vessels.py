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
        a, b, c = list(map(int, input().split()))     
        # s = input().strip()  
        equal = (a+b)/2 
        max_ = max(a, b)
        deliver = max_-equal
        print(math.ceil((deliver)/c))                      
        


if __name__ == "__main__":
    main()