#!/bin/bash

CUTOFF=10
p=$1
LABEL=$2
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
      rm -f $p/joined/joined.fasta
      mkdir -p joined/$i
      python src/join_pairs.py $file >> $p/joined/joined.fasta
    done    
}

cluster () {
  # Cluster joined reads with CDHIT
  echo "clustering"
  sh src/run_cdhit.sh $p/joined/joined.fasta $p/clusters/clusters.fasta
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  echo "Filtering [cutoff = $CUTOFF]"
  python src/filter.py $p/clusters/clusters.fasta $p/clusters/clusters.fasta.clstr $CUTOFF $LABEL > $p/reprs/representatives.fasta
}

init

label_join

cluster

filter