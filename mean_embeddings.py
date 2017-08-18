import sys
import numpy as np

try:
    guard
except:
    print ("Loading data.")
    with open("data/paragram-phrase-XXL.txt", encoding='latin-1') as fh:
        data = np.loadtxt(fh, dtype="object")
    words = {_[1]:_[0] for _ in enumerate(data[:,0])}
    embeddings = data[:,1:].copy().astype("float64")
    guard = None

def compute_mean_embeddings(sent):
    sum_embeddings = 0
    num_embeddings = 0
    for word in sent.split():
        if not word in words:
            print ("Ignoring unknown word: " +  word)
        else:
            num_embeddings += 1
            sum_embeddings = sum_embeddings + embeddings[words[word]]
    if num_embeddings == 0:
        return 0
    return sum_embeddings / num_embeddings

print (compute_mean_embeddings(" ".join(sys.argv[2:])))
