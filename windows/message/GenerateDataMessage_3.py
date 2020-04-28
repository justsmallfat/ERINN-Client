
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('參數說明3')

        selectConfigLabel = tk.Label(windowParameterSet, text="scale_background:")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="{\"linear\", \"log10\"}. The resistivity scale during the sampling phase.")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="pdf_background")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The probability distribution function of the sample.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="a_background")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of pdf_background.")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="b_background")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="upper bound or std (standard deviation) of pdf_background.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="use_hidden_background")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="{True, False}. If True, it will use `hidden_*` to control a_background and b_background.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        testRatioLabel = tk.Label(windowParameterSet, text="hidden_pdf_background")
        testRatioLabel.grid(row=5, column=0, padx=10, pady=10)
        testRatioLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The hidden probability distribution function of the a_background and b_background.")
        testRatioLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        #row4
        geometryUrfLabel = tk.Label(windowParameterSet, text="hidden_a_for_a_background")
        geometryUrfLabel.grid(row=6, column=0, padx=10, pady=10)
        geometryUrfLabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_background for hidden variable a_background.")
        geometryUrfLabelMsg.grid(row=6, column=1, padx=10, pady=10)

        ParaPklLabel = tk.Label(windowParameterSet, text="hidden_b_for_a_background")
        ParaPklLabel.grid(row=7, column=0, padx=10, pady=10)
        ParaPklLabelMsg = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) of hidden_pdf_background for hidden variable a_background.")
        ParaPklLabelMsg.grid(row=7, column=1, padx=10, pady=10)

        #row5
        selectArrayTypeLabel = tk.Label(windowParameterSet, text="hidden_a_for_b_background")
        selectArrayTypeLabel.grid(row=8, column=0, padx=10, pady=10)
        selectArrayTypeLabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_background for hidden variable b_background.")
        selectArrayTypeLabelMsg.grid(row=8, column=1, padx=10, pady=10)

        numKGLabel = tk.Label(windowParameterSet, text="hidden_b_for_b_background")
        numKGLabel.grid(row=9, column=0, padx=10, pady=10)
        numKGLabelMsg = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) for hidden variable b_background.")
        numKGLabelMsg.grid(row=9, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
