
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('參數說明5')

        selectConfigLabel = tk.Label(windowParameterSet, text="num_circle:")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="number of circle angles")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="radius_bound")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="lower bound and upper bound of radius.")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="scale_circle")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="{\"linear\", \"log10\"}. The resistivity scale during the sampling phase.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="pdf_circle")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The probability distribution function of the sample.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        testRatioLabel = tk.Label(windowParameterSet, text="a_circle")
        testRatioLabel.grid(row=5, column=0, padx=10, pady=10)
        testRatioLabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of pdf_circle.")
        testRatioLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        #row4
        geometryUrfLabel = tk.Label(windowParameterSet, text="b_circle")
        geometryUrfLabel.grid(row=6, column=0, padx=10, pady=10)
        geometryUrfLabelMsg = tk.Label(windowParameterSet, text="upper bound or std (standard deviation) of pdf_circle.")
        geometryUrfLabelMsg.grid(row=6, column=1, padx=10, pady=10)

        #row5
        selectArrayTypeLabel = tk.Label(windowParameterSet, text="use_hidden_circle")
        selectArrayTypeLabel.grid(row=8, column=0, padx=10, pady=10)
        selectArrayTypeLabelMsg = tk.Label(windowParameterSet, text="{True, False}. If True, it will use `hidden_*` to control a_circle and b_circle.")
        selectArrayTypeLabelMsg.grid(row=8, column=1, padx=10, pady=10)

        numKGLabel = tk.Label(windowParameterSet, text="hidden_pdf_circle")
        numKGLabel.grid(row=9, column=0, padx=10, pady=10)
        numKGLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The hidden probability distribution function of the a_circle and b_circle.")
        numKGLabelMsg.grid(row=9, column=1, padx=10, pady=10)

        #row4
        Label = tk.Label(windowParameterSet, text="hidden_a_for_a_circle")
        Label.grid(row=10, column=0, padx=10, pady=10)
        LabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_circle for hidden variable a_circle.")
        LabelMsg.grid(row=10, column=1, padx=10, pady=10)

        Label_2 = tk.Label(windowParameterSet, text="hidden_b_for_a_circle")
        Label_2.grid(row=11, column=0, padx=10, pady=10)
        LabelMsg_2 = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) of hidden_pdf_circle for hidden variable a_circle.")
        LabelMsg_2.grid(row=11, column=1, padx=10, pady=10)

        #row5
        Label_3 = tk.Label(windowParameterSet, text="hidden_a_for_b_circle")
        Label_3.grid(row=12, column=0, padx=10, pady=10)
        LabelMsg_3 = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_circle for hidden variable b_circle.")
        LabelMsg_3.grid(row=12, column=1, padx=10, pady=10)

        Label_4 = tk.Label(windowParameterSet, text="hidden_b_for_b_circle")
        Label_4.grid(row=13, column=0, padx=10, pady=10)
        LabelMsg_4 = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) for hidden variable b_circle.")
        LabelMsg_4.grid(row=13, column=1, padx=10, pady=10)

        Label_5 = tk.Label(windowParameterSet, text="configName")
        Label_5.grid(row=14, column=0, padx=10, pady=10)
        LabelMsg_5 = tk.Label(windowParameterSet, text="The Name of file in server.")
        LabelMsg_5.grid(row=14, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
