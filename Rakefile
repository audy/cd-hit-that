#!/usr/bin/env ruby
require 'rake'

# Settin's
sim = 0.8

puts "Sim = #{sim}"

# Codes
require 'rake/clean'
CLEAN.include('out', 'counts.txt')
CLOBBER.include('src/cdhit', 'out', 'counts.txt')

counts = "counts_#{(sim*100).to_i}.txt"
clusters = "out/clusters_#{(sim*100).to_i}.txt"

puts clusters

desc 'Cluster a bunch of reads'
task :default => counts do
  puts "CD-HIT That!"
end

directory 'out' do
  mkdir 'out'
end

file counts => clusters do
  sh "python src/filter.py \
    out/clusters.fasta.clstr \
    out/clusters.fasta 1 > #{counts}"
end

file clusters => ['out/joined.fasta', 'src/cdhit/cd-hit-est'] do
  puts "cluster at #{sim}%"
  cmd = "./src/cdhit/cd-hit-est \
    -i out/joined.fasta \
    -o out/clusters.fasta \
    -c #{sim} \
    -n 10 \
    -T 16 \
    -M 0 \
    -b #{100-sim*100} \
    > #{clusters}"

  sh cmd do |okay|
    if not okay
      rm clusters
    end
  end

end

file 'out/joined.fasta' => 'out' do
  Dir.glob('data/*.fasta').each do |file|
    sh "python src/join_pairs.py #{file} >> out/joined.fasta"
  end
end

desc 'Download & Compile cd-hit-est'
namespace :cdhit do
  # This is messy
  file 'src/cdhit/cd-hit-est' do
    sh 'curl -LO http://www.bioinformatics.org/download.php/cd-hit/cd-hit-v4.3-2010-10-25.tgz'
    sh 'tar -zxvf cd-hit-v4.3-2010-10-25.tgz'
    cd 'cd-hit-v4.3-2010-10-25'
    sh 'make openmp=yes'
    mkdir '../src/cdhit/'
    sh 'mv cd-hit-est ../src/cdhit/'
    cd '..'
    sh 'rm -r cd-hit-v4.3-2010-10-25'
    sh 'rm cd-hit-v4.3-2010-10-25.tgz'
  end
end 