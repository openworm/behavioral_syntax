"""
Created on Sun Sep 20 13:47:35 2015

@author: aidanrocke
"""
import numpy as np
import matplotlib.pyplot as plt

#work with ten biggest:
sizes = list(map(len,toy_seq))
ten_biggest = [sizes.index(i) for i in sizes[30:39]]
subseq = [toy_seq[i] for i in ten_biggest]


relationship = []
for m in subseq:
        
    summary_stats = []
    for i in list(set(map(int,m.split(' ')))):
        P = np.array(ngram_probs(m,str(i))).astype(np.float32)
        #sort probabilities in descending order:
        P = P[np.argsort(-P[:,1])]
        
        matches = list(map(int,P[:,0]))
        errors = error_matrix[i][matches]
        
        N = len(matches)
        #initialize the list that explores the distance_probability relation:
        dist_prob_rel = []
        
        for i in range(N):
            higher = [matches.index(matches[j]) for j in range(N) if errors[i]>=errors[j]]
            lower = [matches.index(matches[j]) for j in range(N) if errors[j]>=errors[i]]
            dist_prob = (np.mean(P[:,1][i]<=P[:,1][[higher]])+np.mean(P[:,1][i]>=P[:,1][[lower]]))/2
            dist_prob_rel.append(dist_prob)
            
        summary_stats.append(np.median(dist_prob_rel))
    
    relationship.append(np.mean(summary_stats))


#relationship:    
np.mean(np.array(summary_stats)>0.7
        
        
#plt.style.use('ggplot')
#plt.plot(errors,P[:,1],color='steelblue')
    
for m in toy_seq:
    summary_stats = []
    for i in list(set(map(int,m.split(' ')))):
        P = np.array(ngram_probs(m,str(i))).astype(np.float32)
        #sort probabilities in descending order:
        P = P[np.argsort(-P[:,1])]

total = np.zeros(39)
for j in range(39):
    nplus,x,y,z = n_grams(toy_seq[j],2)
    L = np.zeros(2*len(x))
    for i in range(len(x)):
        elem = x[i].split(' ')
        n_gram2 = ' '.join([elem[1],elem[0]])
        probs = [calc_prob(toy_seq[34],elem[0],x[i]),calc_prob(toy_seq[34],elem[1],n_gram2)]
        if max(probs) == 0:
            L[i] = 1
        elif min(probs)/max(probs) > 0.60:
            L[i] = 1
        else:
            L[i] = 0
            
    total[j] = np.mean(L)
    

    
   


        
        
    
    
