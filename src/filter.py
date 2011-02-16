import sys
from collections import defaultdict

clust_file = sys.argv[1]
fasta_file = sys.argv[2]
cutoff = int(sys.argv[3])

# Read CLUST File

counts = defaultdict(dict)

with open(clust_file) as handle:
    for line in handle:
        if line.startswith('>'):
            cluster = int(line[1:-1].split()[1])
        else:
            header = line.split()[2].lstrip('>').rstrip('.')
            barcode, read = header.split(':')
            barcode = int(barcode)
            if cluster in counts:
                if barcode in counts[cluster]:
                    counts[cluster][barcode] += 1
                else:
                    counts[cluster][barcode] = 1
            else:
                counts[cluster] = {}
                
# Print table headers
print "-\t",
for barcode in sorted(counts[counts.keys()[0]]):
    print "%s\t" % barcode,
print ''

# Print table values
for cluster in counts:
    print "%s\t" % cluster,
    for barcode in sorted(counts[counts.keys()[0]]):
        try:
            print "%s\t" % counts[cluster][barcode],
        except KeyError:
            print "0\t",
    print ''
print ''