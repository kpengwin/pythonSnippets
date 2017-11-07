#!/usr/bin/python3

import sys
import os

arg = sys.argv[1]

if arg in ['w', 'write', 'create']:
    f=open("file.tmp", "a+")
    f.write("Test text\n")
    f.close()
elif arg in ['r', 'read', 'list']:
    f=open("file.tmp", "r")
    readVal = f.read()
    print("%s" % readVal, end="")
    f.close()
elif arg in ['d', 'delete']:
    os.remove("file.tmp")
