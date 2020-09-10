
import tkinter as tk

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('Parameter Description1')

        selectConfigLabel = tk.Label(windowParameterSet, text="Select config:")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="Select the previously saved parameter configuration file.")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="dataset_dir")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="In this directory, the program will automatically create the train / valid / test directory.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="num_samples")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="number of samples. That is, the total number of synthetic models that will be generated in one round.")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="train_ratio")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="Ratio of the number of samples (num_samples) to be used for training.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="valid_ratio")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="Ratio of the number of samples (num_samples) to be used for validating.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        testRatioLabel = tk.Label(windowParameterSet, text="test_ratio")
        testRatioLabel.grid(row=5, column=0, padx=10, pady=10)
        testRatioLabelMsg = tk.Label(windowParameterSet, text="Ratio of the number of samples (num_samples) to be used for testing.")
        testRatioLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        #row4
        geometryUrfLabel = tk.Label(windowParameterSet, text="geometry_urf")
        geometryUrfLabel.grid(row=6, column=0, padx=10, pady=10)
        geometryUrfLabelMsg = tk.Label(windowParameterSet, text="The path to the urf file is used to construct the electrode array in forward simulation.")
        geometryUrfLabelMsg.grid(row=6, column=1, padx=10, pady=10)

        ParaPklLabel = tk.Label(windowParameterSet, text="Para_pkl")
        ParaPklLabel.grid(row=7, column=0, padx=10, pady=10)
        ParaPklLabelMsg = tk.Label(windowParameterSet, text="The path to the pickle file is used to read and write the necessary parameters used in FW2_5D.")
        ParaPklLabelMsg.grid(row=7, column=1, padx=10, pady=10)

        #row5
        selectArrayTypeLabel = tk.Label(windowParameterSet, text="Select Array Type")
        selectArrayTypeLabel.grid(row=8, column=0, padx=10, pady=10)
        selectArrayTypeLabelMsg = tk.Label(windowParameterSet, text="{\"all_combination\", \"Wenner\"}. Select the electrode pair that matches the array configuration.\n All array types are dipole-dipole settings.")
        selectArrayTypeLabelMsg.grid(row=8, column=1, padx=10, pady=10)

        numKGLabel = tk.Label(windowParameterSet, text="num_k_g")
        numKGLabel.grid(row=9, column=0, padx=10, pady=10)
        numKGLabelMsg = tk.Label(windowParameterSet, text="control the number of wave number (k) and weight (g).")
        numKGLabelMsg.grid(row=9, column=1, padx=10, pady=10)


        selectConfigLabel = tk.Label(windowParameterSet, text="nx:")
        selectConfigLabel.grid(row=10, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="number of mesh in the x direction.")
        selectConfigLabelMsg.grid(row=10, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="nz")
        datasetDirLabel.grid(row=11, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="number of mesh in the z direction.")
        datasetDirLabelMsg.grid(row=11, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="x_kernel_size")
        numSamplesLabel.grid(row=12, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="Kernel size in the x direction.")
        numSamplesLabelMsg.grid(row=12, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="z_kernel_size")
        trainRatioLabel.grid(row=13, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="Kernel size in the z direction.")
        trainRatioLabelMsg.grid(row=13, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
