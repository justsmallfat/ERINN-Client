
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
        datasetDirLabel = tk.Label(windowParameterSet, text="raw_data_dir")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="Walk through this directory (contain subdirectory) to read raw data (pickle file).")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        preprocessLabel = tk.Label(windowParameterSet, text="preprocess")
        preprocessLabel.grid(row=2, column=0, padx=10, pady=10)
        preprocessLabelMsg = tk.Label(windowParameterSet, text=" Add_noise is implemented earlier than log_transform.")
        preprocessLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        performLabel = tk.Label(windowParameterSet, text="preprocess/add_noise/perform")
        performLabel.grid(row=3, column=0, padx=10, pady=10)
        performLabelMsg = tk.Label(windowParameterSet, text="{True, False}. Whether to perform add_noise.")
        performLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        preprocessAddNoiseKwargsRatioLabel = tk.Label(windowParameterSet, text="preprocess/add_noise/kwargs/ratio")
        preprocessAddNoiseKwargsRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        preprocessAddNoiseKwargsRatioLabelMsg = tk.Label(windowParameterSet, text="Noise added to element is proportional to this value.")
        preprocessAddNoiseKwargsRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        #row4
        log_transformLabel = tk.Label(windowParameterSet, text="log_transform")
        log_transformLabel.grid(row=5, column=0, padx=10, pady=10)
        log_transformLabelMsg = tk.Label(windowParameterSet, text="You can also perform log transform in data generator.")
        log_transformLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        log_transformPerformLabel = tk.Label(windowParameterSet, text="log_transform/perform")
        log_transformPerformLabel.grid(row=6, column=0, padx=10, pady=10)
        log_transformPerformLabelMsg = tk.Label(windowParameterSet, text="{True, False}. Whether to perform log_transform.")
        log_transformPerformLabelMsg.grid(row=6, column=1, padx=10, pady=10)

        #row5
        log_transformKwargsInverseLabel = tk.Label(windowParameterSet, text="log_transform/kwargs/inverse")
        log_transformKwargsInverseLabel.grid(row=7, column=0, padx=10, pady=10)
        log_transformKwargsInverseLabelMsg = tk.Label(windowParameterSet, text="{True, False}. Whether to perform an inverse transformation.")
        log_transformKwargsInverseLabelMsg.grid(row=7, column=1, padx=10, pady=10)

        log_transformKwargsInplaceLabel = tk.Label(windowParameterSet, text="log_transform/kwargs/inplace")
        log_transformKwargsInplaceLabel.grid(row=8, column=0, padx=10, pady=10)
        log_transformKwargsInplaceLabelMsg = tk.Label(windowParameterSet, text="{True, False}. Whether to use inplace mode.")
        log_transformKwargsInplaceLabelMsg.grid(row=8, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
