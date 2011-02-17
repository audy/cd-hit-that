import sys

# CDHIT outputs representative sequences in order of cluster
# However, it uses an arbitrary header
# The purpose of this script is to:
#   a.) Verify that claim
#   b.) Fix the headers so they reflect the cluster

# python fix_headers.py clusters.fasta.clstr clusters.fasta

# Load "clusters.fasta.clstr"
r2c = {}
with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            c = line[1:-1]
        else:
            read = line.split()[2][1:].rstrip('.')
            r2c[read] = c

# Load representative sequences
with open(sys.argv[2]) as handle:
    for line in handle:
        if line.startswith('>'):
            read = line[1:-1]
            print ">%s" % r2c[read]
        else:
            print line.strip()