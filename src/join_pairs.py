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

infile = sys.argv[1]
label = sys.argv[2]

with open(infile) as handle:
    for line in handle:
        if line.startswith('>'):
            n = c.next()
            i += 1
            if n == 1:
                print '>%s:%s' % (label, hex(i)[2:])
        else:
            seq[n] += line.strip()
            if n == 1:
                print '%s%s' % (seq[1][::-1], seq[0])
                seq = { 0: '', 1: ''}
