#!/usr/bin/env python

# outputs a FASTQ file but with its filename in the header (sorta)
# Also puts paired reads together with their 5' ends touching
# This is for clustering
# Takes input from STDIN

import sys
import os
from itertools import cycle

c = cycle([0, 1])
seq = { 0: '', 1: ''}

i = 0

for line in sys.stdin:
    if line.startswith('>'):
        i += 1
        print '>%s' % hex(i)[2:]
    else:
        print line.strip()