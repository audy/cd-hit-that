#!/bin/bash

CUTOFF=10
reads=$1
out=$2

echo $reads $out $CUTOFF

init () {
  mkdir -p $out/clusters
  mkdir -p $out/joined
  mkdir -p $out/reprs
}

label_join () {
  # Label and join reads
    for file in reads/*.txt
    do
      echo "Labelling and joining $file"
      mkdir -p joined/$i
      cat $file | python labels.py > $out/joined/$(basename $file).fa
    done
}

cluster () {
  # Cluster joined reads with CDHIT
    for file in $out/joined/*.txt
    do
      echo "Clustering $file"
      sh run_cdhit.sh $file $out/clusters/$(basename $file)
    done
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  for file in $out/clusters/*.txt
  do
    echo "Filtering singletons from $file, cutoff = $CUTOFF"
    python filter.py $file $file.clstr $CUTOFF > $out/reprs/$(basename $file)
  done
}
init

label_join

cluster

filter