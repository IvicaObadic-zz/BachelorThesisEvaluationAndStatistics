import dataset_parser.parser as datasetParser
import nimfa

# target rating matrix in compressed sparse row format
csr_ratings = datasetParser.getSparseRatingsMatrix(
    'C:\\Users\\ivicaobadic\\PycharmProjects\\BachelorThesis\\dataset_parser\\dataset\\yelp_training_set_review.json',60000)
print('Sparse matrix is obtained')

alternatingLeastSquaresNMF = nimfa.Nmf(csr_ratings, seed='random_vcol', rank=60, max_iter=5)

print('Initialization for factorization is finshed, starting with factorization')
res = alternatingLeastSquaresNMF()
print('factorization is done')

