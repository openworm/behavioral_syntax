from vis_functions import grid_plot


import matplotlib.pyplot as plt
from scipy.stats import itemfreq
import numpy as np

all_postures = np.load('/Users/macbook/Documents/c_elegans/all_postures.npy')
  
def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

N = len(all_postures)
cumulative = []

for i in range(N):
    trigram = ngrams(all_postures[0],3)
    
    #looking at the distribution of trigram frequency:
    dist = itemfreq(list(trigram.values()))

    #plot cumulative distribution...see whether it's Zipfian or not:
    cum = 0
    cumsum = np.zeros(len(dist[:,1]))
    for j in range(len(dist[:,1])):
        cum+=dist[:,1][j]
        cumsum[j]=cum/np.dot(dist[:,0],dist[:,1])
    
    cumulative.append(cumsum)
    
grid_plot(cumulative,'CDF','/Users/macbook/Github/behavioral_syntax/plotting/','trigram_dists')

#or view it as a 2d-array:
dist[:,0] = dist[:,0][np.newaxis].T
cumsum = cumsum[np.newaxis].T

np.hstack((dist[:,0],cumsum))

#computing trigram probability: 

#count number of times c12 occurs:
def slicedict(d, s):
    return sum({k:v for k,v in d.items() if k.startswith(s)}.values())

def calc_prob(trigram,tri,vocab_size):
    #vocab_size is set to 90 for the behavioral_syntax paper    
    
    alpha = tri.split(' ')[0:2]
    bi_alpha = ' '.join(alpha)
    
    prob = (slicedict(trigram,tri)+1)/(slicedict(trigram,bi_alpha)+vocab_size)
    
    return prob
    
