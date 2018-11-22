# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, re
penRE = re.compile('pen')
with open(sys.argv[1],'r') as infs:
    for line in infs:
        if penRE.search(line):
            print(line,end='')
            