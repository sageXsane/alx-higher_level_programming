#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    nameslist = dir(hidden_4)
    for name in nameslist:
        if name[0] != '_':
            print("{}".format(name))
