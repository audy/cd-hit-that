#!/bin/bash

CUTOFF=10

label_join () {
  # Label and join reads
  for file in reads/*
  do
    echo "Labelling and joining $file"
    cat $file | python join_pairs.py > joined/$(basename $file).fa
  done
}

cluster () {
  # Cluster joined reads with CDHIT
  for file in joined/*.fa
  do
    echo "Clustering $file"
    sh run_cdhit.sh $file clusters/$(basename $file)
  done
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  for file in clusters/*.fa
  do
    echo "Filtering singletons from $file, cutoff = $CUTOFF"
    python filter.py $file $file.clstr $CUTOFF > reprs/$(basename $file)
  done
}

 label_join

 cluster

 filter