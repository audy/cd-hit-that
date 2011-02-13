import sys
from collections import defaultdict

clust_file = sys.argv[1]
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
            read_to_clust[line[2].rstrip('.')[1:].split(':')[1]] = cluster
            

# Print counts
for cluster in counts:
    if not ((counts[cluster]['N'] > cutoff) and (counts[cluster]['P'] > cutoff)):
        continue
    for group in ('N', 'P'):
        if group in counts[cluster]:
            print >> sys.stderr, "%s\t%s\t%s" % (group, cluster.split()[1], counts[cluster][group])
        else:
            print >> sys.stderr, "%s\t%s\t%s" % (group, cluster.split()[1], 0)
        

# Print out representatives
with open(fasta_file) as handle:
    for line in handle:
        if line.startswith('>'):
            keep = False
            group, read = line.strip().split(':')
            cluster = read_to_clust[read]
            if not ((counts[cluster]['N'] > cutoff) and (counts[cluster]['P'] > cutoff)):
                continue
            else:
                keep = True
                print '>%s Group_%s' % (cluster, group[1:])
        elif keep:
            print line.strip()