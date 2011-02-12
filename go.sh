#!/bin/bash

CUTOFF=10

init () {
  mkdir -p clusters
  mkdir -p joined
  mkdir -p reprs
}

label_join () {
  # Label and join reads
  for file in reads/*.txt
  do
    echo "Labelling and joining $file"
    cat $file | python join_pairs.py > joined/$(basename $file).fa
  done
}

cluster () {
  # Cluster joined reads with CDHIT
  for file in joined/*.txt
  do
    echo "Clustering $file"
    sh run_cdhit.sh $file clusters/$(basename $file)
  done
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  for file in clusters/*.txt
  do
    echo "Filtering singletons from $file, cutoff = $CUTOFF"
    python filter.py $file $file.clstr $CUTOFF > reprs/$(basename $file)
  done
}
init

label_join

cluster

filter