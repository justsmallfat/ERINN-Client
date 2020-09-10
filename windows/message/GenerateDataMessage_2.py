
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('400x300')
        windowParameterSet.title('Parameter Description2')

        selectConfigLabel = tk.Label(windowParameterSet, text="nx:")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="number of mesh in the x direction.")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="nz")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="number of mesh in the z direction.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="x_kernel_size")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="Kernel size in the x direction.")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="z_kernel_size")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="Kernel size in the z direction.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
