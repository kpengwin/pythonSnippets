#!/usr/bin/python3

import sys

a = sys.argv[1]


if a in ['true', 'True', 'TRUE', 'T', '1', 'y']:
    print("True!")
else:
    print("False!")

print("All done, quitting")
