import numpy
from sklearn.metrics import mean_squared_error
from math import sqrt

NUM_RANDOM_MATRICES_GENERATED = 5
NUM_EPOCHS = 25
RANDOM_PREDICTIONS_PATH = "C:/Users/ivicaobadic/Desktop/Diplomska/Final predictions/random/{mode}/"
RMSE_RESULTS_PATH = "C:/Users/ivicaobadic/Desktop/Diplomska/Final RMSE results/"
RANDOM_RMSE_RESULTS_PATH = "C:/Users/ivicaobadic/Desktop/Diplomska/Final RMSE results/Random/{mode}"
MODES = ['Column_min_max', 'Matrix_min_max']

BASE_PREDICTIONS_PATHS = [
    "C:/Users/ivicaobadic/Desktop/Diplomska/Final predictions/whole_test_set/predictions_",
     "C:/Users/ivicaobadic/Desktop/Diplomska/Final predictions/much_reviews/predictions_",
     "C:/Users/ivicaobadic/Desktop/Diplomska/Final predictions/few_reviews/predictions_"
     ]

OUTPUT_FILE_NAMES = [
    'rmse_output_whole.txt',
    'rmse_output_much.txt',
    'rmse_output_few.txt'
]

def rmse(target, predictions):
    return sqrt(mean_squared_error(target, predictions))


print('Generating random rmse results')
#####GENERATE RMSE SCORES FOR THE RANDOM MATRICES
for mode in MODES:
    for sample in ['few.txt', 'much.txt', 'whole.txt']:
        fileToWritePath = RANDOM_RMSE_RESULTS_PATH.replace('{mode}', mode) + '/' + sample
        fileToWrite = open(fileToWritePath, mode = 'w')
        for j in range(0, NUM_RANDOM_MATRICES_GENERATED):
            filepath = RANDOM_PREDICTIONS_PATH.replace('{mode}', mode) + str(j) + '/' + sample
            predictions = numpy.loadtxt(filepath)
            target_values = predictions[:, 0]
            predicted_values = predictions[:, 1]
            fileToWrite.write(str(rmse(target_values, predicted_values)) + '\n')

        fileToWrite.close()


print('Generating computed factors rmse results')
####GENERATE RMSE SCORES FOR THE LEARNED ITEM FACTORS BY CONVOLUTIONAL NEURAL NETWORK
for j in range(0, len(BASE_PREDICTIONS_PATHS)):
    RMSE_OUTPUT_FILE = open(RMSE_RESULTS_PATH + OUTPUT_FILE_NAMES[j], mode='w')
    for EPOCH in range(1, NUM_EPOCHS+1):
        predictions_path = BASE_PREDICTIONS_PATHS[j] + str(EPOCH) + '.txt'
        predictions = numpy.loadtxt(predictions_path)
        target_values = predictions[:, 0]
        predicted_values = predictions[:, 1]
        rmse_metric = rmse(target_values, predicted_values)
        RMSE_OUTPUT_FILE.write(str(rmse_metric))
        RMSE_OUTPUT_FILE.write('\n')

