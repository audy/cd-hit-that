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
    for file in $p/*.fasta
    do
      echo "Labelling and joining $file"
      mkdir -p joined/$i
      cat $file | python join_pairs.py > $p/joined/$(basename $file)
    done
}

cluster () {
  # Cluster joined reads with CDHIT
    for file in $p/joined/*.fasta
    do
      echo "Clustering $file"
      sh run_cdhit.sh $file $p/clusters/$(basename $file)
    done
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  for file in $p/clusters/*.fasta
  do
    echo "Filtering singletons from $file, cutoff = $CUTOFF"
    python filter.py $file $file.clstr $CUTOFF > $p/reprs/$(basename $file)
  done
}

init

label_join

cluster

filter
