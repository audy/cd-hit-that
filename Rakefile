#!/usr/bin/env ruby
require 'rake'

SIM = 40 # Default, 
CUTOFF = 5000 # Reads per cluster (total)
MIN_READ_LEN = 70 # bases

# Codes
require 'rake/clean'
CLEAN.include('out', 'counts.txt')
CLOBBER.include('src/cdhit', 'out', 'counts.txt')

counts = "counts_#{SIM}.txt"
clusters = "out/clusters_#{SIM}"
representatives = "out/representatives_#{SIM}.fasta"

desc 'Cluster at num%'
task :cluster, :num do |t, args|
  SIM = args.num # set SIM
  counts = "counts_#{SIM}.txt"
  clusters = "out/clusters_#{SIM}"
  representatives = "out/representatives_#{SIM}.fasta"
  Rake.application.invoke_task(:default)
end

desc "Cluster at #{SIM}%"
task :default => [counts, representatives] do
  puts "CD-HIT That!"
end

directory 'out' do
  mkdir 'out'
end

file counts => [clusters, representatives] do
  # Make table
  sh "python src/filter.py \
    #{clusters}.clstr \
    #{clusters} 1 > #{counts}"
end

file representatives => clusters do
  # Re-label representative sequences
  sh "python src/fix_headers.py \
    #{clusters}.clstr \
    #{clusters} #{CUTOFF} \
    > out/representatives_#{SIM}.fasta"
end

file clusters => ['out/joined.fasta', 'src/cdhit/cd-hit-est'] do
  puts "cluster at #{SIM}%"
 
  cmd = "./src/cdhit/cd-hit-est \
    -i out/joined.fasta \
    -o #{clusters} \
    -c 0.#{SIM} \
    -n 10 \
    -T 16 \
    -M 0 \
    > /dev/null"

  sh cmd do |okay|
    if not okay
      rm clusters
    end
  end

end

file 'out/joined.fasta' => 'out' do
  Dir.glob('data/*.fasta').each do |file|
    sh "python src/join_label.py #{file} >> out/joined.fasta"
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
