# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of the permutation (not strictly needed for the logic, but part of the input format)
    n = int(input())
    
    # Read the permutation as a list of integers
    a = list(map(int, input().split()))
    
    # The core insight: The first element a[0] can never be moved.
    # For the array to be sorted into [1, 2, 3, ...], a[0] must be 1.
    # If it is, sorting is possible. If not, it's impossible.
    if a[0] == 1:
        print("YES")
    else:
        print("NO")