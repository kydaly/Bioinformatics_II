def deBruijn(patterns):
  """From an input of kmers construct a deBruijn graph in an adjacency list with
  glued together nodes and their respective edges"""
  adj_list = {} # initialize the adjacency list
  
  for kmer in patterns:
    node = kmer[:-1]
    if node in adj_list:
      pass
    else:
      adj_list[node] = []
  for node in adj_list:
    for k in patterns:
      prefix = k[:-1]
      suffix = k[1:]
      edge = k[1:]
      if node == prefix and edge == suffix:
          adj_list[node].append(suffix)
  for k in adj_list.copy():
    if not adj_list[k]:
      del adj_list[k]
  return adj_list