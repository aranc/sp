import numpy as np

try:
    guard
except:
    print "Loading data."
    data = np.loadtxt("data/paragram-phrase-XXL.txt", dtype="object")
    words = data[:,0].copy()
    embeddings = data[:,1:].copy().astype("float64")
    guard = None
