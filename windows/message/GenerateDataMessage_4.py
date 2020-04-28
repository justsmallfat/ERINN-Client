
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title('參數說明4')

        selectConfigLabel = tk.Label(windowParameterSet, text="num_rect:")
        selectConfigLabel.grid(row=0, column=0, padx=10, pady=10)
        selectConfigLabelMsg = tk.Label(windowParameterSet, text="number of rectangles")
        selectConfigLabelMsg.grid(row=0, column=1, padx=10, pady=10)

        #row2
        datasetDirLabel = tk.Label(windowParameterSet, text="w_range")
        datasetDirLabel.grid(row=1, column=0, padx=10, pady=10)
        datasetDirLabelMsg = tk.Label(windowParameterSet, text="width range (x direction).")
        datasetDirLabelMsg.grid(row=1, column=1, padx=10, pady=10)

        numSamplesLabel = tk.Label(windowParameterSet, text="h_range")
        numSamplesLabel.grid(row=2, column=0, padx=10, pady=10)
        numSamplesLabelMsg = tk.Label(windowParameterSet, text="height range (z direction).")
        numSamplesLabelMsg.grid(row=2, column=1, padx=10, pady=10)

        trainRatioLabel = tk.Label(windowParameterSet, text="scale_rect")
        trainRatioLabel.grid(row=3, column=0, padx=10, pady=10)
        trainRatioLabelMsg = tk.Label(windowParameterSet, text="{\"linear\", \"log10\"}. The resistivity scale during the sampling phase.")
        trainRatioLabelMsg.grid(row=3, column=1, padx=10, pady=10)

        validRatioLabel = tk.Label(windowParameterSet, text="pdf_rect")
        validRatioLabel.grid(row=4, column=0, padx=10, pady=10)
        validRatioLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The probability distribution function of the sample.")
        validRatioLabelMsg.grid(row=4, column=1, padx=10, pady=10)

        testRatioLabel = tk.Label(windowParameterSet, text="a_rect")
        testRatioLabel.grid(row=5, column=0, padx=10, pady=10)
        testRatioLabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of pdf_rect.")
        testRatioLabelMsg.grid(row=5, column=1, padx=10, pady=10)

        #row4
        geometryUrfLabel = tk.Label(windowParameterSet, text="b_rect")
        geometryUrfLabel.grid(row=6, column=0, padx=10, pady=10)
        geometryUrfLabelMsg = tk.Label(windowParameterSet, text="upper bound or std (standard deviation) of pdf_rect.")
        geometryUrfLabelMsg.grid(row=6, column=1, padx=10, pady=10)

        #row5
        selectArrayTypeLabel = tk.Label(windowParameterSet, text="use_hidden_rect")
        selectArrayTypeLabel.grid(row=8, column=0, padx=10, pady=10)
        selectArrayTypeLabelMsg = tk.Label(windowParameterSet, text="{True, False}. If True, it will use `hidden_*` to control a_rect and b_rect.")
        selectArrayTypeLabelMsg.grid(row=8, column=1, padx=10, pady=10)

        numKGLabel = tk.Label(windowParameterSet, text="hidden_pdf_rect")
        numKGLabel.grid(row=9, column=0, padx=10, pady=10)
        numKGLabelMsg = tk.Label(windowParameterSet, text="{\"uniform\", \"normal\"}. The hidden probability distribution function of the a_rect and b_rect.")
        numKGLabelMsg.grid(row=9, column=1, padx=10, pady=10)

        #row4
        Label = tk.Label(windowParameterSet, text="hidden_a_for_a_rect")
        Label.grid(row=10, column=0, padx=10, pady=10)
        LabelMsg = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_rect for hidden variable a_rect.")
        LabelMsg.grid(row=10, column=1, padx=10, pady=10)

        Label_2 = tk.Label(windowParameterSet, text="hidden_b_for_a_rect")
        Label_2.grid(row=11, column=0, padx=10, pady=10)
        LabelMsg_2 = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) of hidden_pdf_rect for hidden variable a_rect.")
        LabelMsg_2.grid(row=11, column=1, padx=10, pady=10)

        #row5
        Label_3 = tk.Label(windowParameterSet, text="hidden_a_for_b_rect")
        Label_3.grid(row=12, column=0, padx=10, pady=10)
        LabelMsg_3 = tk.Label(windowParameterSet, text="lower bound or mu (mean) of hidden_pdf_rect for hidden variable b_rect.")
        LabelMsg_3.grid(row=12, column=1, padx=10, pady=10)

        Label_4 = tk.Label(windowParameterSet, text="hidden_b_for_b_rect")
        Label_4.grid(row=13, column=0, padx=10, pady=10)
        LabelMsg_4 = tk.Label(windowParameterSet, text="upper bound or std(standard deviation) for hidden variable b_rect.")
        LabelMsg_4.grid(row=13, column=1, padx=10, pady=10)

    def fun(self):
        return "Hello world."
