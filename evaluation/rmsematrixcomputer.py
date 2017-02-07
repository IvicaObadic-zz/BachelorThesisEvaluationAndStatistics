import numpy as np

FACTORIZATION_FACTORS_FILE = \
    "C:/Users/ivicaobadic/Desktop/Diplomska/Output/Factorization/Factors computed on whole set/test_items_factors_computed_on_whole_set_with_factorization.txt"

BEST_LEARNED_FACTORS_FILE = "C:/Users/ivicaobadic/Desktop/Diplomska/Output/ConvNet/Factors epochs output/Learning_rate_0.001, filters_length=4,unknown_items/factor_predictions_23.txt"

def get_factors_as_matrix(filename):
    factors_matrix = np.zeros((2308, 20), dtype='float32')

    count = 0
    for line in open(filename):
        parts = line.strip().split('\t')
        factors_matrix[count] = np.asarray(parts[1:], dtype='float32')
        count += 1

    return factors_matrix

factorization_factors = get_factors_as_matrix(FACTORIZATION_FACTORS_FILE)
learned_factors = get_factors_as_matrix(BEST_LEARNED_FACTORS_FILE)

print(np.sqrt(np.mean((factorization_factors - learned_factors)**2)))



