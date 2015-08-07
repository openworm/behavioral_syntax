def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output
  
  
#sort trigrams 
merriam = ngrams(all_postures[0],3)

sorted_merriam = sorted(merriam.items(), key=operator.itemgetter(1),reverse=True)
