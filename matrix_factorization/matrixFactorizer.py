import dataset_parser.parser as datasetParser

sparseMatrix = datasetParser.getSparseRatingsMatrix(
    'C:\\Users\\ivicaobadic\\PycharmProjects\\BachelorThesis\\dataset_parser\\dataset\\yelp_training_set_review.json'
    )

print(sparseMatrix)