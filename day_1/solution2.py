def alter_merge(w1,w2):
    x=""
    n=min(len(w1),len(w2))
    for i in range (n):
      x=x+w1[i]+w2[i]

    return(x+w1[i+1:]+w2[i+1:])