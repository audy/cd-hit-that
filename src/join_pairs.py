#!/usr/bin/env python

# outputs a FASTQ file but with its filename in the header (sorta)
# Also puts paired reads together with their 5' ends touching
# This is for clustering
# Takes input from STDIN

import sys
import os
from itertools import cycle

import string
_complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

c = cycle([0, 1])
seq = { 0: '', 1: ''}

i = 0

infile = sys.argv[1]
minimum_read_length = int(sys.argv[2])

f_num = int(infile.split('_')[-1].split('.')[0])
kept, skipped = 0, 0

with open(infile) as handle:
    for line in handle:
        if line.startswith('>'):
            n = c.next()
            i += 1
            if n == 1:
                header = '>%s:%s' % (f_num, hex(i)[2:])
        else:
            seq[n] += line.strip()
            if n == 1:
                # Reverse-complement 3' pair
                seq[1] = seq[1].translate(_complement)[::-1]
                
                # Make sure reads are minimum length
                if (len(seq[0]) >= minimum_read_length) \
                    and (len(seq[1]) >= minimum_read_length):
                    print header
                    print '%s%s' % (seq[1], seq[0])
                    kept +=1
                else:
                    skipped +=1
                
                seq = { 0: '', 1: ''}


print >> sys.stderr, "kept: %.2f percent of pairs (%s : %s)" % (float(kept)/(skipped + kept), skipped, kept)