#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif len(argv) > 1:
        print("{} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
