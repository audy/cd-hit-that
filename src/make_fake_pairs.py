import sys
import string

fn = sys.argv[1]

sequence = []
complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

with open(fn) as handle:
    for line in handle:
        if line.startswith('>'):
            if len(sequence) > 0:
                sequence = ''.join(sequence)
                forward = sequence[:101][11:]
                reverse = sequence[-101:][:-11]
                s =  "%s%s" % (reverse, forward)
                print s
                sequence = []
            print ">%s" % line.split(';')[-1].strip()
        else:
            sequence.append(line.strip())
