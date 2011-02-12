import sys
from collections import defaultdict

clust_file = sys.argv[2]
fasta_file = sys.argv[2]
cutoff = int(sys.argv[3])

# count clusters
counts = {}
read_to_clust = {}
with open(clust_file) as handle:
    for line in handle:
        if line.startswith('>'):
            cluster = line[1:-1]
            counts[cluster] = defaultdict(int)
        else:
            line = line.split()
            group = line[2][1:].rstrip('.').split(':')[0]
            counts[cluster][group] += 1
            read_to_clust[line[2].rstrip('.')] = cluster
            
# Print out representatives

with open(fasta_file) as handle:
    for line in handle:
        if line.startswith('>'):
            group, read = line.strip().split(':')
            cluster = read_to_clust[read]
            count = counts[cluster][group]
            print >> sys.stderr, "%s\t%s" % (cluster, count)
