#!/usr/bin/python3

import sys
import re


searchItem = re.compile("(%s)" % sys.argv[1])
with open(sys.argv[2], "rU") as file:
    for line in file:
        if searchItem.search(line):
            print("%s" % (searchItem.sub(r"***\1***", line)), end="")




