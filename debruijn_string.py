def de_bruijn(k, text):
  """Construct a de_brujin graph given an integer k, and a string text"""
  # make a list of kmers of length k
  kmers = []
  edges = []
  nodes = []
  adj_list = {}
  # edges are suffixs and nodes are prefixs
  for i in range(len(text) - k + 1): # creates a list of all kmers in the text
    kmer = text[i:i+k]
    kmers.append(kmer)
    edge = kmer[1:k]
    edges.append(edge)

  # make a list of nodes that does not have duplicates
  for kmer in kmers:
    node = kmer[:-1]
    if node in nodes:
      pass
    else:
      nodes.append(node)
  # go through all the nodes and compare it to each prefix in the kmer list    
  for node in nodes:
    adj_vals = []
    for i in range(len(text) - k + 1):
      # check if the prefix of kmer is the same as node 
      if text[i:i+k-1] == node:
        adj_vals.append(edges[i]) # adds the suffix of the current kmer (edge)
    adj_vals.sort()
    adj_list[node] = adj_vals
  return adj_list
