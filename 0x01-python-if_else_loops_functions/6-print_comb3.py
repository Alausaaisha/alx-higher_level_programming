#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i < j:
            print('{}'.format(i), end='')
            print('{}'.format(j), end=', ')
print('{}{}'.format(i + 1, j))
