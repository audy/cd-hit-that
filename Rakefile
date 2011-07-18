#!/usr/bin/env ruby
require 'rake'

Reads_Glob = 'data/*'
Output = 'out'

SIM = 80 # Default, 
CUTOFF = 5000 # Reads per cluster (total)
MIN_READ_LEN = 70 # bases

Counts = "counts_#{SIM}.txt"
Clusters = "out/clusters_#{SIM}"
Representatives = "out/representatives_#{SIM}.fasta"

# Codes
require 'rake/clean'
CLEAN.include('out', 'counts.txt')
CLOBBER.include('src/cdhit', 'out', 'counts.txt')

desc 'Cluster at num%'
task :cluster, :num do |t, args|
  SIM = args.num # set SIM
  Counts = "counts_#{SIM}.txt"
  Clusters = "out/clusters_#{SIM}"
  Representatives = "out/representatives_#{SIM}.fasta"
  Rake.application.invoke_task(:default)
end

desc "Cluster at #{SIM}%"
task :default => [Counts, Representatives] do
  puts "CD-HIT That!"
end

directory Output do
  mkdir Output
end

file Counts => [Clusters, Representatives] do
  # Make table
  sh "python src/filter.py \
    #{Clusters}.clstr \
    #{Clusters} 1 > #{Counts}"
end

file Representatives => Clusters do
  # Re-label representative sequences
  sh "python src/fix_headers.py \
    #{Clusters}.clstr \
    #{Clusters} #{CUTOFF} \
    > out/representatives_#{SIM}.fasta"
end

file Clusters => ['out/joined.fasta', 'src/cdhit/cd-hit-est'] do
  puts "cluster at #{SIM}%"
 
  cmd = "./src/cdhit/cd-hit-est \
    -i out/joined.fasta \
    -o #{Clusters} \
    -c 0.#{SIM} \
    -n 10 \
    -T 16 \
    -M 0 \
    -b #{100-SIM} \
    > /dev/null"

  sh cmd do |okay|
    if not okay
      rm Clusters
    end
  end

end

file 'out/joined.fasta' => 'out' do
  Dir.glob(Reads_Glob).each do |file|
    sh 'rm -f out/joined.fasta'
    sh "python src/join_pairs.py #{file} #{MIN_READ_LEN} >> out/joined.fasta"
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
