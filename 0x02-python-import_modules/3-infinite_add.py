#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ans = 0
    for i in range(1, len(sys.argv)):
        ans += int(sys.argv[i])
    print(f"{ans}")
