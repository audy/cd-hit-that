sim=$1
cdhit_overhang=0.78
wordsize=10
cores=16
cdhit='./src/cdhit/cd-hit-est'
input=$2
output=$3

$cdhit \
  -i $input \
  -o $output \
  -c 0.$sim \
  -n $wordsize \
  -T $cores \
  -s 0.$cdhit_overhang \
  -M 0 
