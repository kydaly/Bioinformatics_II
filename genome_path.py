def genomepath(kmers):
  """a list of kmers is put in and a genome put together with those kmers is 
  output. The kmers after the first must have their second and second to last
  match the previous kmer."""
  count = 0 # used to make string for previous kmer added to genome
  genome = kmers[0] # initiates the genome to be constructed
  for i, kmer in enumerate(kmers):
    partial = kmer[0:-1] # the string kmer except for the last character
    previous = genome[count+1:] # the previously added kmer except for the first letter
    if partial == previous: # tests for the kmer to overlap with the previously added kmer
      addon = kmer[-1] # the non-overlapping character
      genome += addon # adds non-overlapping character to genome
      count += 1 # increases count to make the next previous variable
  return genome