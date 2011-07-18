#!/usr/bin/env python

from itertools import cycle, count

import sys

c = cycle([1,2,3,4])
co = count()

with open(sys.argv[1]) as handle:
  for line in handle:
    n = c.next()
   
    if n == 1:
      print '>%s' % co.next()
    elif n == 2:
      print line.rstrip()
