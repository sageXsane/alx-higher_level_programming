#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    if (arguments == 0):
        print("0 arguments.")
    elif (arguments == 1):
        print("1 argument:")
    else:
        print(f"{arguments} arguments:")

    for i in range(1, arguments + 1):
        print(i, ": ", sys.argv[i], sep="")
