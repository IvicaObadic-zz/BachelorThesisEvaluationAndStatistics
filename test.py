import nimfa
from scipy.sparse import *
import os
docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
indptr = [0]
indices = []
data = []
vocabulary = {}
for d in docs:
     for term in d:
         index = vocabulary.setdefault(term, len(vocabulary))
         indices.append(index)
         data.append(1)
     indptr.append(len(indices))


####another test####

a = [[1,0,2], [2,4,0], [8,4,0], [0, 0, 0]]


indptr = [0]
indices = []
data = []
for arr in a:
    for i in range(0, len(arr)):
        if arr[i] == 0 :
            continue
        data.append(arr[i])
        indices.append(i)

    indptr.append(len(data))


sparseMatrix = csr_matrix((data, indices, indptr), dtype=int)
print(sparseMatrix.todense())
