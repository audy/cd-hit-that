#!/usr/bin/env python

import sys
import string
_complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

sequence = False
with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            if sequence:
                a = sequence[11:100-11]
                b = sequence[::-1][11:100-11]
                print ">%s\n%s%s\n" % (header, b, a)

            sequence = '' # slow way!
            header = line[1:-1].split(';')[-1]
        else:
            sequence += line.strip()
