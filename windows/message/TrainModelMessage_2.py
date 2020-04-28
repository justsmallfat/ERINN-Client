
import tkinter as tk

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('參數說明1')

        selectConfigLabel = tk.Label(windowParameterSet, text="custom_NN")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="custom keras model")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="train_dir")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="training dataset.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="valid_dir")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="validation dataset.")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="model_dir")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="In this directory, the program will automatically create the logs/predictions/weights directory.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="pre_trained_weights")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="hdf5 file saved the weight of the keras model. If you don't want to use pre-trained weights, use an empty string.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
