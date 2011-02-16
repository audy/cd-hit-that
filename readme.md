# CD-HIT That

- Run CDHIT on a buncha files. Oh yeah, they're paired-end 
- Create a table of sequences per cluster per file
- Input data is paired-end, interleaved, FASTA reads which are joined together with their 5' ends touching and clustered.

# Usage:

- Reads go in `data/` and have to be in FASTA format
- Filenames need to have a number in them between a `_` and `.`. For example: `reads_blah_blah_033.fasta`. This is for the column header in the output table (it will be `33`). It goes without saying that this number should be unique.

To change parameters such has similarity requirement, edit the Rakefile.

The table will be saved as `counts.txt`

Type `rake clean` to start over.