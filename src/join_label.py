#!/usr/bin/env python

import sys

INFILE = sys.argv[1]
F_NUM = int(infile.split('_')[-1].split('.')[0]) # This is crap

i = 0

with open(INFILE) as handle:
    for line in handle:
        if line.startswith('>'):
            i += 1
            print '>%s:%s' % (f_num, hex(i)[2:])
        else:
            print line.strip()