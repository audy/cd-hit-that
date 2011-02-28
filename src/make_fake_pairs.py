import sys
import string

fn = sys.argv[1]
MIN_READ_LENGTH = int(sys.argv[2])
sequence = []
keep = False
complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

with open(fn) as handle:
    for line in handle:
        if line.startswith('>'):
            if keep:
                print header
                print sequence
                
            if len(sequence) > 0:
                sequence = ''.join(sequence)
                forward = sequence[:101][11:]
                reverse = sequence[-101:][:-11]
                sequence =  "%s%s" % (reverse, forward)
                if (len(forward) >= MIN_READ_LENGTH) \
                    and (len(reverse) >= MIN_READ_LENGTH):
                    keep = True
            keep = False
            sequence = []
            header = ">%s" % line.split(';')[-1].strip()
        else:
            sequence.append(line.strip())
