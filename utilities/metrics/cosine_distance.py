import numpy as np

def cosine_distance(a,b):
  """
  the cosine similarity of two vectors.
  """

  cost = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
  
  return cost
