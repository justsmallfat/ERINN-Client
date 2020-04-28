
import tkinter as tk

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('參數說明1')

        selectConfigLabel = tk.Label(windowParameterSet, text="num_gpu")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="number of gpu")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="batch_size")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="Size for mini-batch gradient descent.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="num_epochs")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="number of epochs.")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="optimizer")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="Select the optimizer in keras.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="learning_rate")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="Optimizer learning rate.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        testRatioLabel = tk.Label(windowParameterSet, text="loss")
        testRatioLabel.grid(row=5, column=0, padx=10, pady=10)
        testRatioLabelMsg = tk.Label(windowParameterSet, text="loss function for calculate gradient.")
        testRatioLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        #row4
        geometryUrfLabel = tk.Label(windowParameterSet, text="configName")
        geometryUrfLabel.grid(row=6, column=0, padx=10, pady=10)
        geometryUrfLabelMsg = tk.Label(windowParameterSet, text="The Name of file in server.")
        geometryUrfLabelMsg.grid(row=6, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
