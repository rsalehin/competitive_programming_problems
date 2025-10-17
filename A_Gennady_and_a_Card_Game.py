import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

# Fast input reading
input = sys.stdin.readline

# ========== MAIN ==========
def main():     
    rank, suite = list(input().strip())
    table = list(input().strip().split())       
    for card in table:
        if card[0] in rank or card[1] in suite:
            print('YES')
            return 
    print('NO')  
        


if __name__ == "__main__":
    main()