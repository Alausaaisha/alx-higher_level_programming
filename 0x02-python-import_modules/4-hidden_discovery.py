#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for i in names:
        if i[0] == '_':
            pass
        else:
            print(i)
