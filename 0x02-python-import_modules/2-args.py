#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv) - 1
    if leng == 0:
        print("0 arguments.")
    elif leng == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif leng > 1:
        print("{} arguments:".format(leng))
        for i in range(1, leng + 1):
            print("{}: {}".format(i, argv[i]))
