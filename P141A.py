# -------------------------------
# Codeforces Python Boilerplate
# -------------------------------
import sys
from collections import defaultdict, Counter
from math import *
from itertools import *
from bisect import *
from io import StringIO

# Main solve function (customize this for each problem)
def solve():
    guest = input().strip()
    host = input().strip()
    pile = input().strip()
    
    combined = guest + host
    if Counter(combined) == Counter(pile):
        print("YES")
    else:
        print("NO")

# Boilerplate runner
def main():
    # For multiple test cases, uncomment:
    # t = int(input().strip())
    # for _ in range(t):
    #     solve()
    
    # For single test case
    solve()

# -------------------------------
# Local Test Helper
# -------------------------------
def run_tests():
    tests = [
        ("""SANTACLAUS
DEDMOROZ
SANTAMOROZDEDCLAUS
""", "YES\n"),
        ("""PAPAINOEL
JOULUPUKKI
JOULNAPAOILELUPUKKI
""", "NO\n"),
        ("""BABBONATALE
FATHERCHRISTMAS
BABCHRISTMASBONATALLEFATHER
""", "NO\n"),
    ]
    
    for i, (input_data, expected) in enumerate(tests, 1):
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()
        main()
        result = sys.stdout.getvalue()
        assert result == expected, f"Test {i} failed: expected {expected!r}, got {result!r}"
        print(f"Test {i} passed ✅")

if __name__ == "__main__":
    if "test" in sys.argv:  # run with: python file.py test
        run_tests()
    else:
        main()
