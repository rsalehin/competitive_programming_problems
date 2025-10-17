def main():
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().split())
        ans = (n * m + 1) // 2
        print(ans)

if __name__ == "__main__":
    main()
