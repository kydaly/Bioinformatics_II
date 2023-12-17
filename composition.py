def string_composition(k, text):
  """Function takes in a number for length of kmer (k) and a string. The output
  is each kmer in the string including duplicates"""
  k_list = []
  for i in range(len(text) - k + 1):
    kmer = text[i:i+k]
    k_list.append(kmer)
  return k_list