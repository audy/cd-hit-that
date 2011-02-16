require 'rake/clean'

CLEAN.include('out', 'counts.txt')

sim = 0.95

desc 'Cluster a bunch of reads'
task :default => 'counts.txt' do
  
end

directory 'out' do
  mkdir 'out'
end

file 'counts.txt' => 'out/clusters.txt' do
  sh "python src/filter.py \
    out/clusters.fasta.clstr \
    out/clusters.fasta 1 > counts.txt"
end

file 'out/clusters.txt' => ['out/joined.fasta', 'src/cdhit/cd-hit-est' do
  sh "./src/cdhit/cd-hit-est \
    -i out/joined.fasta \
    -o out/clusters.fasta \
    -c #{sim} \
    -n 10 \
    -T 16 \
    -s 0.78 \
    -M 0 \
    > out/clusters.txt"
end

file 'out/joined.fasta' => 'out' do
  Dir.glob('data/*.fasta').each do |file|
    sh "python src/join_pairs.py #{file} >> out/joined.fasta"
  end
end

desc 'Download & Compile cd-hit-est'
file 'src/cdhit/cd-hit-est' => 'src/cdhit' do
  puts 'Building CD-HIT'
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