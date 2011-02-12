#!/bin/bash

CUTOFF=10
p=$1

echo $p

init () {
  mkdir -p $p/clusters
  mkdir -p $p/joined
  mkdir -p $p/reprs
}

label_join () {
  # Label and join reads
    for file in $p/reads/*.txt
    do
      echo "Labelling and joining $file"
      mkdir -p joined/$i
      cat $file | python labels.py > $p/joined/$(basename $file).fa
    done
}

cluster () {
  # Cluster joined reads with CDHIT
    for file in $p/joined/*.txt
    do
      echo "Clustering $file"
      sh run_cdhit.sh $file $p/clusters/$(basename $file)
    done
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  for file in $p/clusters/*.txt
  do
    echo "Filtering singletons from $file, cutoff = $CUTOFF"
    python filter.py $file $file.clstr $CUTOFF > $p/reprs/$(basename $file)
  done
}

init

label_join

cluster

filter