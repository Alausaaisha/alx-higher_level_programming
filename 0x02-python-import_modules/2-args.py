#!/usr/bin/python3
import sys
if __name__ == "__main__":
    LengthOfArg = len(sys.argv)
    if LengthOfArg == 1:
        print(f'{LengthOfArg - 1} arguments.')
    elif LengthOfArg == 2:
        print(f'{LengthOfArg - 1} argument:')
        for i in range(1, LengthOfArg):
            print(f'{i}: {sys.argv[i]}')
    elif LengthOfArg > 2:
        print(f'{LengthOfArg - 1} arguments:')
        for i in range(1, LengthOfArg):
            print(f'{i}: {sys.argv[i]}')
