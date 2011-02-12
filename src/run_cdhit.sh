sim=95
cdhit_overhang=0.78
wordsize=10
cores=16
cdhit='./src/cdhit/cd-hit-est'
input=$1
output=$2

$cdhit \
  -i $input \
  -o $output \
  -c 0.$sim \
  -n $wordsize \
  -T $cores \
  -s 0.$cdhit_overhang \
  > /dev/null
