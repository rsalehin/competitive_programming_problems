import sys
input = sys.stdin.readline

def main():
    t = int(input().strip())
    for _ in range(t):
        a, b, c = map(int, input().split())

        time_elevator1 = abs(a - 1)
        time_elevator2 = abs(b - c) + abs(c - 1)

        if time_elevator1 < time_elevator2:
            print(1)
        elif time_elevator1 > time_elevator2:
            print(2)
        else:
            print(3)

if __name__ == "__main__":
    main()
