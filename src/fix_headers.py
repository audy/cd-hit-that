import sys
from collections import defaultdict

# CDHIT outputs representative sequences in order of cluster
# However, it uses an arbitrary header
# The purpose of this script is to:
#   a.) Verify that claim
#   b.) Fix the headers so they reflect the cluster

# python fix_headers.py clusters.fasta.clstr clusters.fasta

# Load "clusters.fasta.clstr"
r2c = {}
cc = defaultdict(int)
CUTOFF = int(sys.argv[3])

with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            c = line[1:-1]
        else:
            read = line.split()[2][1:].rstrip('.')
            r2c[read] = c
            cc[c] += 1

# Load representative sequences
with open(sys.argv[2]) as handle:
    for line in handle:
        if line.startswith('>'):
            keep = True
            read = line[1:-1]
            count = cc[r2c[read]]
            if count < CUTOFF:
              keep = False
              continue
            print ">%s %s" % (r2c[read].replace(' ', '_'), cc[r2c[read]])
        elif keep:
            print line.strip()
