def overlap(patterns):
  """function creates an adjacency list for suffixs and prefixs that overlap
     making an overlap graph"""
  prefixs = {}
  adj_list = {} # initialize a dictionary as the adjacency list
  for kmer in patterns:
    prefix = kmer[:-1]
    prefixs[kmer] = prefix

  for kmer in patterns:
    suffix = kmer[1:]
    adj_list[kmer] = []
    for key, value in prefixs.items():
      if suffix == value:
        adj_list[kmer].append(key)
  for k in adj_list.copy():
    if not adj_list[k]:
      del adj_list[k]

  return adj_list