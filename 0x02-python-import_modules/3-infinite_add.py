#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = 0
    lengthOfArg = len(sys.argv)
    for i in range(1, lengthOfArg):
        add += int(sys.argv[i])
    print(add)
