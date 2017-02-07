import numpy
import matplotlib.pyplot as plt

rmse_root_file = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Final RMSE results\\'
plots_source_file = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Plots\\'

def generateLinePlot(
        title,
        xlabel,
        ylabel,
        yvalues,
        output_filename
):

    x_values = numpy.arange(1, len(yvalues) + 1, step=1)
    plt.plot(x_values, yvalues)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(output_filename, format='jpg', dpi= 1000)
    plt.show()


def generateLinePlotWithTwoLines(
        title,
        xlabel,
        ylabel,
        yvalues1,
        ylegend1,
        yvalues2,
        ylegend2,
        output_filename
):
    x_values = numpy.arange(1, len(yvalues1) + 1, step=1)

    plt.plot(x_values, yvalues1)
    plt.plot(x_values, yvalues2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend([ylegend1, ylegend2], loc = 'upper right')
    plt.savefig(output_filename, format='jpg', dpi = 1000)
    plt.show()

def generate_bar_plot(title, xlabel, ylabel, x_values, y_values, output_filename):
    plt.bar(x_values, y_values, width=1/1.5, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(output_filename, format='jpg', dpi = 1000)
    plt.show()

def generate_line_plot_between_conv_net_errors(sourcefile = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Output\\ConvNet\\training and test errors'):

    training_errors = []
    test_errors = []
    for line in open(sourcefile):
        parts = line.strip().split('\t')
        training_errors.append(float(parts[0]))
        test_errors.append(float(parts[1]))

    filepath = plots_source_file + '\\Conv net output\\train_test_error.jpg'
    generateLinePlotWithTwoLines(
        'Conv net epoch output',
        'Epoch',
        'RMSE',
        training_errors,
        'RMSE on training set',
        test_errors,
        'RMSE on test set',
        filepath)


def generate_histogram(title, xlabel, ylabel, values, bins, output_filename):

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.hist(values, bins, alpha = 0.8)
    plt.savefig(output_filename, format='jpg', dpi = 1000)
    plt.show()

def plot_two_histograms_together(title, xlabel, ylabel, values1, values2, bins, output_filename):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.hist(values1, bins, alpha=1.0, color='#990000')
    plt.hist(values2, bins, alpha=0.5, color='#660033')
    plt.legend(['Least common businesses votes distribution', 'Most common businesses votes distribution'], loc='upper right')
    plt.savefig(output_filename, format='jpg', dpi=1000)
    plt.show()

def generate_line_plot_for_rmse_error():
    few_rmse_file = rmse_root_file + 'rmse_output_few.txt'
    much_rmse_file = rmse_root_file + 'rmse_output_much.txt'
    whole_rmse_file = rmse_root_file + 'rmse_output_whole.txt'

    filepath = plots_source_file + '\\Conv net output\\few_rmse_test_error.jpg'

    few_rmse_array = numpy.loadtxt(few_rmse_file, delimiter='\t')
    generateLinePlot(
        'RMSE error on test set for business with only few reviews',
        'Epoch',
        'RMSE',
        few_rmse_array,
        filepath
        )

    filepath = plots_source_file + '\\Conv net output\\much_rmse_test_error.jpg'

    few_rmse_array = numpy.loadtxt(much_rmse_file, delimiter='\t')
    generateLinePlot(
        'RMSE error on test set for business with much reviews',
        'Epoch',
        'RMSE',
        few_rmse_array,
        filepath
    )

    filepath = plots_source_file + '\\Conv net output\\whole_rmse_test_error.jpg'

    whole_rmse_file = numpy.loadtxt(whole_rmse_file, delimiter='\t')
    generateLinePlot(
        'RMSE error on whole test set',
        'Epoch',
        'RMSE',
        whole_rmse_file,
        filepath
    )
