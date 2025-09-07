def solve():
    nums = list(map(int, input().split()))
    max_num = max(nums)
    orig = []
    for num in nums:
        if max_num - num > 0:
            orig.append(max_num - num)
    print(" ".join(map(str, orig)))
solve() 