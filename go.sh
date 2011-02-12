#!/bin/bash

CUTOFF=1
p=$1
echo $p

init () {
  for p in N P
  do
    mkdir -p $p/clusters
    mkdir -p $p/joined
    mkdir -p $p/reprs
  done
}

label_join () {
  # Label and join reads
  for p in N P
  do
    for file in $p/*.fasta
    do
      echo "Labelling and joining $file"
      rm -f $p/joined/joined.fasta
      mkdir -p joined/$i
      python src/join_pairs.py $file $p >> $p/joined/joined.fasta
    done
  done
  
  cat P/joined/joined.fasta N/joined/joined.fasta > both.fasta
  
}

cluster () {
  # Cluster joined reads with CDHIT
  echo "clustering"
  sh src/run_cdhit.sh both.fasta clusters.fasta
}

filter () {
  # Filter out rep. reads that belong to clusters only consting of themself
  echo "Filtering [cutoff = $CUTOFF]"
  python src/filter.py clusters.fasta clusters.fasta.clstr $CUTOFF > representatives.fasta
}

init

label_join

cluster

filter