import numpy as np

NUM_ITEMS = 11537

NUM_FACTORS = 20

COLUMN_GENERATED_RANDOM_VALUES = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Random generated factors matrices\\Column_min_max\\'
MATRIX_GENERATED_RANDOM_VALUES = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Random generated factors matrices\\Matrix_min_max\\'

def generate_random_matrices_with_min_max_column_range():
    factors_matrix = get_computed_item_factors_matrix()
    max_column_values = np.amax(factors_matrix, axis=0)
    min_column_values = np.amin(factors_matrix, axis=0)
    print(max_column_values)
    print(min_column_values)
    for i in range(0, 5):
        random_matrix = np.zeros((NUM_ITEMS, NUM_FACTORS), dtype='float32')
        for j in range(0, NUM_FACTORS):
            random_column_values = np.random.uniform(min_column_values[j], max_column_values[j] + 0.0001, size=(1, NUM_ITEMS))
            random_matrix[:,j] = random_column_values

        filepath = COLUMN_GENERATED_RANDOM_VALUES + 'random_factors_' + str(i) + '.txt'
        np.savetxt(filepath, random_matrix, delimiter='\t')


def generate_random_matrices_in_min_max_range():
    factors_matrix = get_computed_item_factors_matrix()
    for i in range(0, 5):
        random_matrix = np.random.uniform(np.amin(factors_matrix), np.amax(factors_matrix), size=(11537, 20))
        filepath = MATRIX_GENERATED_RANDOM_VALUES + 'random_factors_' + str(i) + '.txt'
        np.savetxt(filepath, random_matrix, delimiter='\t')


def get_computed_item_factors_matrix():
    factors_matrix = np.zeros(shape=(NUM_ITEMS, NUM_FACTORS), dtype='float32')
    count = 0
    for line in open('C:/Users/ivicaobadic/Desktop/Diplomska/LibRec algoritmi/Computed Librec model/itemFactors.txt'):
        if len(line) > 0:
            parts = line.strip().split(':')
            item_factors = np.asarray(parts[1].split(','), dtype='float32')
            factors_matrix[count] = item_factors
        count += 1
    return factors_matrix


generate_random_matrices_with_min_max_column_range()
generate_random_matrices_in_min_max_range()