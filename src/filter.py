import sys
from collections import defaultdict
from pprint import pprint
clust_file = sys.argv[1]
fasta_file = sys.argv[2]
cutoff = int(sys.argv[3])

# Read CLUST File

counts = {}

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
barcodes = max(counts.values(), key=len).keys()
print "-\t",
for barcode in barcodes:
    print "%s\t" % barcode,
print ''

# Print table values
for cluster in counts:
    print "%s\t" % cluster,
    for barcode in barcodes:
        try:
            val = counts[cluster][barcode]
        except KeyError:
            val = '0'
            print >> sys.stderr, "%s, %s" % (cluster, barcode)
        print "%s\t" % val,
    print ''
print ''