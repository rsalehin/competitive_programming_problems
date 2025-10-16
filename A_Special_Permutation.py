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
        arr = []
        middle = n//2 
        for i in range(n, 0, -1):
            arr.append(str(i))
        if n%2 == 1:
            arr[0], arr[middle] = arr[middle], arr[0]
        print(" ".join(arr))                     
        


if __name__ == "__main__":
    main()