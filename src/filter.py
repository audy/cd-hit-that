import sys

reads = sys.argv[1]
cluster_file = sys.argv[2]
cutoff = int(sys.argv[3])
label = sys.argv[4]

# Count number of clusters
counts = {}
reads_to_clust = {}
with open(sys.argv[2]) as handle:
    for line in handle:
        if line.startswith('>'):
            cluster = line.strip()
            counts[cluster] = set()
        else:
            read = line.split()[2].rstrip('.')
            counts[cluster].add(read)
            reads_to_clust[read] = cluster
            
with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            keep = False
            read = line.strip()
            cluster = reads_to_clust[read]
            if len(counts[cluster]) > cutoff:
                keep = True
                print '>%s' % label
        elif keep:
            print line.strip()
            
for cluster in counts:
    print >> sys.stderr, "%s, %s" % (cluster, counts[cluster])