
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime
import numpy as np
from SupportFiles import Tools
from numpy import arange
from numpy import linspace
from matplotlib import pyplot
import matplotlib.pyplot as plt
from scipy.stats import norm, truncnorm, uniform

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from windows.message import GenerateDataMessage_1
from windows.message import GenerateDataMessage_2
from windows.message import GenerateDataMessage_3
from windows.message import GenerateDataMessage_4
from windows.message import GenerateDataMessage_5

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('1000x750')
        windowParameterSet.title('生成資料')
        tab_parent = ttk.Notebook(windowParameterSet)

        tabs = [{"title":"generic setting_1","tab":ttk.Frame(tab_parent)},
                {"title":"background","tab":ttk.Frame(tab_parent)},
                {"title":"rectangle","tab":ttk.Frame(tab_parent)},
                {"title":"circle","tab":ttk.Frame(tab_parent)},
                {"title":"action","tab":ttk.Frame(tab_parent)}]

        for tempTab in tabs:
            tab_parent.add(tempTab["tab"], text=tempTab["title"])

        yaml_data = Tools.getConFigYaml_data('config.yml')
        global serverURL
        serverURL = f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}'

        global photo
        photo = tk.PhotoImage(file ='D:/kevin_paper/project/ERINN-Client/question.gif')
        global rootSendData
        # values
        global datasetDirPath
        global numSamplesNum
        global trainRatioNum
        global validRatioNum
        global testRatioNum
        global geometryUrfVar
        global ParaPklVar
        global arrayTypeValue
        global numKGNum
        global NXNum
        global NZNum
        global xKernelSizeNum
        global zKernelSizeNum

        global scaleBackgroundValue
        global pdfBackgroundValue
        global aBackgroundNum
        global bBackgroundNum
        global hiddenPdfBackgroundValue
        global useHiddenBackgroundValue
        global hidden_a_for_a_backgroundNum
        global hidden_a_for_b_backgroundNum
        global hidden_b_for_a_backgroundNum
        global hidden_b_for_b_backgroundNum

        global num_rectNum
        global w_range_1
        global w_range_2
        global h_range_1
        global h_range_2
        global scale_rectValue
        global pdf_rectValue
        global a_rectNum
        global b_rectNum
        global hidden_pdf_rectValue
        global useHiddenRectValue
        global hidden_a_for_a_rectNum
        global hidden_b_for_a_rectNum
        global hidden_a_for_b_rectNum
        global hidden_b_for_b_rectNum

        global num_circleNum
        global radius_boundNum_1
        global radius_boundNum_2
        global scale_circleValue
        global pdf_circleValue
        global a_circleNum
        global b_circleNum
        global hidden_pdf_circleValue
        global useHiddencircleValue
        global hidden_a_for_a_circleNum
        global hidden_b_for_a_circleNum
        global hidden_a_for_b_circleNum
        global hidden_b_for_b_circleNum
        global configNameValue

        def getConfigData(configName):
            global rootSendData
            tabOneSendData = {'configFileName': comboxlist.get()}
            r = requests.post(f'{serverURL}/getConfigData', data=tabOneSendData)
            print(f"getConfigData : {r.text}")
            rootSendData = json.loads(r.text)
            loadDataRefreshView()

        def getBoardFrame(boardType, scaleType, a, b):
            f = Figure(figsize=(3,3), dpi=50)
            print(f'boardType = {boardType } a {a} b {b}')

            x_axis_size = int(abs(b-a+1))
            if x_axis_size<50:
                x_axis_size = 50
            # x_axis = linspace(a, b, x_axis_size)
            x_axis = linspace(a, b, x_axis_size)
            if 'normal'==boardType:
                print(f'normal')
                x_axis = linspace(0, a*2, x_axis_size)
                if scaleType == 'linear':
                    _a = (0 - a) / b
                    _b = (np.inf - a) / b
                    pd = truncnorm(_a, _b, loc=a, scale=b)
                elif scaleType == 'log10':
                    pd = norm(loc=a, scale=b)
                else:
                    raise ValueError('You did not input enough or correct keyword argument.')


                y_axis = pd.pdf(x_axis)

                # mid = (b+a)/2
                # y_axis = norm.pdf(x_axis, mid)
                # plot data
                pyplot = f.add_subplot(111)
                # print(f'x_axis = {x_axis } y_axis {y_axis} a {a} b {b}')
                pyplot.plot(x_axis, y_axis)
            else:
                print(f'uniform')
                # x_axis = linspace(uniform.ppf(a), uniform.ppf(b), x_axis_size)
                if a>b:
                    return f

                pd = uniform(a, b-a)
                y_axis = pd.pdf(x_axis)
                pyplot = f.add_subplot(111)
                pyplot.plot(x_axis, y_axis)
                r = pd.rvs(size=x_axis_size)
                # print(f'x_axis = {x_axis } y_axis {y_axis} a {a} b {b} r {r}')
                pyplot.hist(r, density=True, histtype='stepfilled', alpha=0.2)
                pyplot.legend(loc='best', frameon=False)
                # x_axis = linspace(bBackgroundNum.get(), aBackgroundNum.get(), 100)
                # mid = (bBackgroundNum.get()+aBackgroundNum.get())/2
                # y_axis = uniform.pdf(x_axis, mid)
                # pyplot.plot(x_axis, y_axis)
            return f

        def reLoadView(self):
            print(f"reLoadView {useHiddenBackgroundValue}")
            global rootSendData
            tabIndex = 4
            rowIndex = 7

            rowIndex = rowIndex + 1
            BackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="background")
            BackgroundLabel.grid(row=rowIndex, column=1, padx=5, pady=5)
            rectLabel = tk.Label(tabs[tabIndex]["tab"], text="rect")
            rectLabel.grid(row=rowIndex, column=2, padx=5, pady=5)
            circleLabel = tk.Label(tabs[tabIndex]["tab"], text="circle")
            circleLabel.grid(row=rowIndex, column=3, padx=5, pady=5)

            rowIndex = rowIndex + 1
            titleLabel = tk.Label(tabs[tabIndex]["tab"], text="scaleType")
            titleLabel.grid(row=rowIndex, column=0, padx=5, pady=5)
            BackgroundValueLabel = tk.Label(tabs[tabIndex]["tab"], text=scaleBackgroundValue.get())
            BackgroundValueLabel.grid(row=rowIndex, column=1, padx=5, pady=5)
            BackgroundValueLabel = tk.Label(tabs[tabIndex]["tab"], text=scale_rectValue.get())
            BackgroundValueLabel.grid(row=rowIndex, column=2, padx=5, pady=5)
            BackgroundValueLabel = tk.Label(tabs[tabIndex]["tab"], text=scale_circleValue.get())
            BackgroundValueLabel.grid(row=rowIndex, column=3, padx=5, pady=5)

            rowIndex = rowIndex + 1
            titleLabel = tk.Label(tabs[tabIndex]["tab"], text="pdf")
            titleLabel.grid(row=rowIndex, column=0, padx=5, pady=5)
            f = getBoardFrame(pdfBackgroundValue.get(), scaleBackgroundValue.get(), aBackgroundNum.get(), bBackgroundNum.get())
            canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
            canvas.draw()
            canvas.get_tk_widget().grid(row=rowIndex, column=1, padx=5, pady=5)
            f = getBoardFrame(pdf_rectValue.get(), scale_rectValue.get(), a_rectNum.get(), b_rectNum.get())
            canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
            canvas.draw()
            canvas.get_tk_widget().grid(row=rowIndex, column=2, padx=5, pady=5)
            f = getBoardFrame(pdf_circleValue.get(), scale_circleValue.get(), a_circleNum.get(), b_circleNum.get())
            canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
            canvas.draw()
            canvas.get_tk_widget().grid(row=rowIndex, column=3, padx=5, pady=5)

            rowIndex = rowIndex + 1
            titleLabel = tk.Label(tabs[tabIndex]["tab"], text="Use Hidden for a")
            titleLabel.grid(row=rowIndex, column=0, padx=5, pady=5)
            if useHiddenBackgroundValue.get():
                f = getBoardFrame(hiddenPdfBackgroundValue.get(), hiddenPdfBackgroundValue.get(), hidden_a_for_a_backgroundNum.get(), hidden_b_for_a_backgroundNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=1, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=1, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=1, padx=15, pady=15)
            if useHiddenRectValue.get():
                f = getBoardFrame(hidden_pdf_rectValue.get(), hidden_pdf_rectValue.get(), hidden_a_for_a_rectNum.get(), hidden_b_for_a_rectNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=2, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=2, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
            if useHiddencircleValue.get():
                f = getBoardFrame(hidden_pdf_circleValue.get(), hidden_pdf_circleValue.get(), hidden_a_for_a_circleNum.get(), hidden_b_for_a_circleNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=3, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=3, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=3, padx=15, pady=15)


            rowIndex = rowIndex + 1
            titleLabel = tk.Label(tabs[tabIndex]["tab"], text="Use Hidden for b")
            titleLabel.grid(row=rowIndex, column=0, padx=5, pady=5)
            if useHiddenBackgroundValue.get():
                f = getBoardFrame(hiddenPdfBackgroundValue.get(), hiddenPdfBackgroundValue.get(), hidden_a_for_b_backgroundNum.get(), hidden_b_for_b_backgroundNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=1, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=1, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=1, padx=15, pady=15)
            if useHiddenRectValue.get():
                f = getBoardFrame(hidden_pdf_rectValue.get(), hidden_pdf_rectValue.get(), hidden_a_for_b_rectNum.get(), hidden_b_for_b_rectNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=2, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=2, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
            if useHiddencircleValue.get():
                f = getBoardFrame(hidden_pdf_circleValue.get(), hidden_pdf_circleValue.get(), hidden_b_for_a_circleNum.get(), hidden_b_for_b_circleNum.get())
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=3, padx=5, pady=5)
            else:
                f = Figure(figsize=(3,3), dpi=50)
                canvas = FigureCanvasTkAgg(f, tabs[tabIndex]["tab"])
                canvas.draw()
                canvas.get_tk_widget().grid(row=rowIndex, column=3, padx=5, pady=5)
                messageLabel = tk.Label(tabs[tabIndex]["tab"], text="No use")
                messageLabel.grid(row=rowIndex, column=3, padx=15, pady=15)


        # tab_parent.bind("<<NotebookTabChanged>>", reLoadView)
        def creatMessageView_1():
            GenerateDataMessage_1.ParameterSetWindow(window)
        def creatMessageView_3():
            GenerateDataMessage_3.ParameterSetWindow(window)
        def creatMessageView_4():
            GenerateDataMessage_4.ParameterSetWindow(window)
        def creatMessageView_5():
            GenerateDataMessage_5.ParameterSetWindow(window)

        #Tab1
        tabIndex = 0
        rowIndex = 0
        btnParameterSet = tk.Button(tabs[tabIndex]["tab"], image = photo, command=creatMessageView_1)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        selectConfigLabel = tk.Label(tabs[tabIndex]["tab"], text="選擇設定檔:")
        selectConfigLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        comvalue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        comboxlist = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=comvalue)  # 初始化
        r = requests.post(f'{serverURL}/getConfigs')
        list = r.text
        comboxlist["values"] = list.split(',')
        comboxlist.grid(row=rowIndex, column=1, padx=15, pady=15)
        comboxlist.current(0)  # 選擇第一個
        comboxlist.bind("<<ComboboxSelected>>", getConfigData)

        rowIndex = rowIndex + 1
        datasetDirLabel = tk.Label(tabs[tabIndex]["tab"], text="dataset_dir")
        datasetDirLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        datasetDirPath = tk.StringVar(value="../data/raw_data")
        datasetDirEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=datasetDirPath)
        datasetDirEntry.grid(row=rowIndex, column=1, padx=15, pady=15)

        numSamplesLabel = tk.Label(tabs[tabIndex]["tab"], text="num_samples")
        numSamplesLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        numSamplesNum = tk.StringVar(value="50")
        numSamplesEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=numSamplesNum)
        numSamplesEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        trainRatioLabel = tk.Label(tabs[tabIndex]["tab"], text="train_ratio")
        trainRatioLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        trainRatioNum = tk.StringVar(value="0.8")
        trainRatioEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=trainRatioNum)
        trainRatioEntry.grid(row=rowIndex, column=1, padx=15, pady=15)

        validRatioLabel = tk.Label(tabs[tabIndex]["tab"], text="valid_ratio")
        validRatioLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        validRatioNum = tk.StringVar(value="0.1")
        validRatioEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=validRatioNum)
        validRatioEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        testRatioLabel = tk.Label(tabs[tabIndex]["tab"], text="test_ratio")
        testRatioLabel.grid(row=rowIndex, column=4, padx=15, pady=15)
        testRatioNum = tk.StringVar(value="0.1")
        testRatioEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=testRatioNum)
        testRatioEntry.grid(row=rowIndex, column=5, padx=15, pady=15)

        rowIndex = rowIndex + 1
        geometryUrfLabel = tk.Label(tabs[tabIndex]["tab"], text="geometry_urf")
        geometryUrfLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        geometryUrfVar = tk.StringVar(value="../config/geo.urf")
        geometryUrfEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=geometryUrfVar)
        geometryUrfEntry.grid(row=rowIndex, column=1, padx=15, pady=15)

        ParaPklLabel = tk.Label(tabs[tabIndex]["tab"], text="Para_pkl")
        ParaPklLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        ParaPklVar = tk.StringVar(value="../config/Para.pkl")
        ParaPklEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=ParaPklVar)
        ParaPklEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        selectArrayTypeLabel = tk.Label(tabs[tabIndex]["tab"], text="選擇 Array Type")
        selectArrayTypeLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        arrayTypeValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        arrayTypeBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=arrayTypeValue)  # 初始化
        arrayTypeBoxList["values"] = ["all_combination", "Wenner"]
        arrayTypeBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        arrayTypeBoxList.current(0)  # 選擇第一個

        numKGLabel = tk.Label(tabs[tabIndex]["tab"], text="num_k_g")
        numKGLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        numKGNum = tk.StringVar(value="4")
        numKGEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=numKGNum)
        numKGEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        NXLabel = tk.Label(tabs[tabIndex]["tab"], text="nx:")
        NXLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        global NXNum
        NXNum = tk.StringVar(value=140)
        NXEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=NXNum)
        NXEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        xKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], text="x_kernel_size:")
        xKernelSizeLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        xKernelSizeNum = tk.StringVar(value="3")
        xKernelSizeEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=xKernelSizeNum)
        xKernelSizeEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        NZLabel = tk.Label(tabs[tabIndex]["tab"], text="nz:")
        NZLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        NZNum = tk.StringVar(value="30")
        NZEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=NZNum)
        NZEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        zKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], text="z_kernel_size:")
        zKernelSizeLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        zKernelSizeNum = tk.StringVar(value="30")
        zKernelSizeEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=zKernelSizeNum)
        zKernelSizeEntry.grid(row=rowIndex, column=3, padx=15, pady=15)
        tab_parent.pack(expand=2, fill='both')

        tabIndex = tabIndex + 1
        rowIndex = 0
        btnParameterSet = tk.Button(tabs[tabIndex]["tab"], image = photo, command=creatMessageView_3)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        scaleBackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="Scale background")
        scaleBackgroundLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        scaleBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scaleBackgroundBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=scaleBackgroundValue)  # 初始化
        scaleBackgroundBoxList["values"] = ["linear", "log10"]
        scaleBackgroundBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        scaleBackgroundBoxList.bind("<<ComboboxSelected>>", reLoadView)
        scaleBackgroundBoxList.current(0)  # 選擇第一個
        pdfBackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="pdf background")
        pdfBackgroundLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        pdfBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdfBackgroundBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=pdfBackgroundValue)  # 初始化
        pdfBackgroundBoxList["values"] = ["uniform", "normal"]
        pdfBackgroundBoxList.grid(row=rowIndex, column=3, padx=15, pady=15)
        # pdfBackgroundBoxList.current(0)  # 選擇第一個
        pdfBackgroundBoxList.bind("<<ComboboxSelected>>", reLoadView)

        rowIndex = rowIndex + 1
        aBackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="a_background:")
        aBackgroundLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        aBackgroundNum = tk.DoubleVar(value=10)
        aBackgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=aBackgroundNum)
        aBackgroundEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        bBackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="b_background:")
        bBackgroundLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        bBackgroundNum = tk.DoubleVar(value=1)
        bBackgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=bBackgroundNum)
        bBackgroundEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hiddenPdfBackgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_pdf_background")
        hiddenPdfBackgroundLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hiddenPdfBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hiddenPdfBackgroundBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=hiddenPdfBackgroundValue)  # 初始化
        hiddenPdfBackgroundBoxList["values"] = ["uniform", "normal"]
        hiddenPdfBackgroundBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        hiddenPdfBackgroundBoxList.current(0)  # 選擇第一個
        hiddenPdfBackgroundBoxList.bind("<<ComboboxSelected>>", reLoadView)
        useHiddenBackgroundValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        hidden_a_for_a_backgroundNum = tk.DoubleVar(value=0.001)
        hidden_b_for_a_backgroundNum = tk.DoubleVar(value=1000)
        hidden_a_for_b_backgroundNum = tk.DoubleVar(value=0.001)
        hidden_b_for_b_backgroundNum = tk.DoubleVar(value=100)
        c1 = tk.Checkbutton(tabs[tabIndex]["tab"], text='use_hidden_background', variable=useHiddenBackgroundValue, command=lambda:reLoadView(self), onvalue=1, offvalue=0)
        c1.grid(row=rowIndex, column=2, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hidden_a_for_a_backgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_a_rect:")
        hidden_a_for_a_backgroundLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_a_backgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_a_backgroundNum)
        hidden_a_for_a_backgroundEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_b_for_a_backgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_a_rect:")
        hidden_b_for_a_backgroundLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_a_backgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_a_backgroundNum)
        hidden_b_for_a_backgroundEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hidden_a_for_b_backgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_b_rect:")
        hidden_a_for_b_backgroundLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_b_backgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_b_backgroundNum)
        hidden_a_for_b_backgroundEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_b_for_b_backgroundLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_b_rect:")
        hidden_b_for_b_backgroundLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_b_backgroundEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_b_backgroundNum)
        hidden_b_for_b_backgroundEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        tabIndex = tabIndex + 1
        rowIndex = 0
        btnParameterSet = tk.Button(tabs[tabIndex]["tab"], image = photo, command=creatMessageView_4)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        num_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="num_rect:")
        num_rectLabel.grid(row=0, column=0, padx=15, pady=15)
        num_rectNum = tk.IntVar(value=1)
        num_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=num_rectNum)
        num_rectEntry.grid(row=0, column=1, padx=15, pady=15)

        rowIndex = rowIndex + 1
        w_rangeLabel = tk.Label(tabs[tabIndex]["tab"], text="w_range :")
        w_rangeLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        w_range_1 = tk.IntVar(value=1)
        w_range_1Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=w_range_1)
        w_range_1Entry.grid(row=rowIndex, column=1, padx=15, pady=15)
        w_range_2 = tk.IntVar(value=140)
        w_range_2Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=w_range_2)
        w_range_2Entry.grid(row=rowIndex, column=2, padx=15, pady=15)

        rowIndex = rowIndex + 1
        h_rangeLabel = tk.Label(tabs[tabIndex]["tab"], text="h_range :")
        h_rangeLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        h_range_1 = tk.IntVar(value=1)
        h_range_1Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=h_range_1)
        h_range_1Entry.grid(row=rowIndex, column=1, padx=15, pady=15)
        h_range_2 = tk.IntVar(value=30)
        h_range_2Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=h_range_2)
        h_range_2Entry.grid(row=rowIndex, column=2, padx=15, pady=15)

        rowIndex = rowIndex + 1
        scale_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="scale_rect")
        scale_rectLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        scale_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scale_rectBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=scale_rectValue)  # 初始化
        scale_rectBoxList["values"] = ["linear", "log10"]
        scale_rectBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        scale_rectBoxList.current(0)  # 選擇第一個
        scale_rectBoxList.bind("<<ComboboxSelected>>", reLoadView)
        pdf_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="pdf_rect")
        pdf_rectLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        pdf_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdf_rectBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=pdf_rectValue)  # 初始化
        pdf_rectBoxList["values"] = ["uniform", "normal"]
        pdf_rectBoxList.grid(row=rowIndex, column=3, padx=15, pady=15)
        pdf_rectBoxList.current(0)  # 選擇第一個
        pdf_rectBoxList.bind("<<ComboboxSelected>>", reLoadView)

        rowIndex = rowIndex + 1
        a_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="a_rect :")
        a_rectLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        a_rectNum = tk.IntVar(value=1)
        a_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=a_rectNum)
        a_rectEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        b_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="b_rect :")
        b_rectLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        b_rectNum = tk.IntVar(value=1)
        b_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=b_rectNum)
        b_rectEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hidden_pdf_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_pdf_rect")
        hidden_pdf_rectLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_pdf_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hidden_pdf_rectBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=hidden_pdf_rectValue)  # 初始化
        hidden_pdf_rectBoxList["values"] = ["uniform", "normal"]
        hidden_pdf_rectBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_pdf_rectBoxList.current(0)  # 選擇第一個
        hidden_pdf_rectBoxList.bind("<<ComboboxSelected>>", reLoadView)
        useHiddenRectValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        c2 = tk.Checkbutton(tabs[tabIndex]["tab"], text='use_hidden_rect', variable=useHiddenRectValue, command=lambda:reLoadView(self), onvalue=1, offvalue=0)
        c2.grid(row=rowIndex, column=2, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hidden_a_for_a_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_a_rect :")
        hidden_a_for_a_rectLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_a_rectNum = tk.DoubleVar(value=0.001)
        hidden_a_for_a_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_a_rectNum)
        hidden_a_for_a_rectEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_b_for_a_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_a_rect :")
        hidden_b_for_a_rectLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_a_rectNum = tk.DoubleVar(value=1000)
        hidden_b_for_a_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_a_rectNum)
        hidden_b_for_a_rectEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        rowIndex = rowIndex + 1
        hidden_a_for_b_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_b_rect :")
        hidden_a_for_b_rectLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_b_rectNum = tk.DoubleVar(value=0.001)
        hidden_a_for_b_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_b_rectNum)
        hidden_a_for_b_rectEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_b_for_b_rectLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_b_rect :")
        hidden_b_for_b_rectLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_b_rectNum = tk.DoubleVar(value=1000)
        hidden_b_for_b_rectEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_b_rectNum)
        hidden_b_for_b_rectEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        # finalDataTab
        tabIndex = tabIndex + 1
        rowIndex = 0
        btnParameterSet = tk.Button(tabs[tabIndex]["tab"], image = photo, command=creatMessageView_5)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        num_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="num_circle :")
        num_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        num_circleNum = tk.IntVar(value=0)
        num_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=num_circleNum)
        num_circleEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        radius_boundLabel = tk.Label(tabs[tabIndex]["tab"], text="radius_bound :")
        radius_boundLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        radius_boundNum_1 = tk.IntVar(value=5)
        radius_bound_1Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=radius_boundNum_1)
        radius_bound_1Entry.grid(row=rowIndex, column=3, padx=15, pady=15)
        radius_boundNum_2 = tk.IntVar(value=20)
        radius_bound_2Entry = tk.Entry(tabs[tabIndex]["tab"], textvariable=radius_boundNum_2)
        radius_bound_2Entry.grid(row=rowIndex, column=4, padx=15, pady=15)

        #row2
        rowIndex = rowIndex + 1
        scale_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="scale_circle")
        scale_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        scale_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scale_circleBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=scale_circleValue)  # 初始化
        scale_circleBoxList["values"] = ["linear", "log10"]
        scale_circleBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        scale_circleBoxList.current(0)  # 選擇第一個
        scale_circleBoxList.bind("<<ComboboxSelected>>", reLoadView)
        pdf_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="pdf_circle")
        pdf_circleLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        pdf_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdf_circleBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=pdf_circleValue)  # 初始化
        pdf_circleBoxList["values"] = ["uniform", "normal"]
        pdf_circleBoxList.grid(row=rowIndex, column=3, padx=15, pady=15)
        pdf_circleBoxList.current(0)  # 選擇第一個
        pdf_circleBoxList.bind("<<ComboboxSelected>>", reLoadView)

        #row3
        rowIndex = rowIndex + 1
        a_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="a_circle :")
        a_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        a_circleNum = tk.IntVar(value=1)
        a_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=a_circleNum)
        a_circleEntry.grid(row=rowIndex, column=1, padx=15, pady=15)

        b_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="b_circle :")
        b_circleLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        b_circleNum = tk.IntVar(value=1)
        b_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=b_circleNum)
        b_circleEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        #row4
        rowIndex = rowIndex + 1
        hidden_pdf_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_pdf_circle")
        hidden_pdf_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_pdf_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hidden_pdf_circleBoxList = ttk.Combobox(tabs[tabIndex]["tab"], textvariable=hidden_pdf_circleValue)  # 初始化
        hidden_pdf_circleBoxList["values"] = ["uniform", "normal"]
        hidden_pdf_circleBoxList.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_pdf_circleBoxList.current(0)  # 選擇第一個
        hidden_pdf_circleBoxList.bind("<<ComboboxSelected>>", reLoadView)
        # hidden_pdf_circleBoxList.grid(row=rowIndex, column=3, padx=15, pady=15)
        useHiddencircleValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        c2 = tk.Checkbutton(tabs[tabIndex]["tab"], text='use_hidden_circle', variable=useHiddencircleValue, command=lambda:reLoadView(self), onvalue=1, offvalue=0)
        c2.grid(row=rowIndex, column=2, padx=15, pady=15)

        #row5
        rowIndex = rowIndex + 1
        hidden_a_for_a_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_a_circle :")
        hidden_a_for_a_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_a_circleNum = tk.DoubleVar(value=0.001)
        hidden_a_for_a_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_a_circleNum)
        hidden_a_for_a_circleEntry.grid(row=rowIndex, column=1, padx=15, pady=15)
        hidden_b_for_a_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_a_circle :")
        hidden_b_for_a_circleLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_a_circleNum = tk.DoubleVar(value=1000)
        hidden_b_for_a_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_a_circleNum)
        hidden_b_for_a_circleEntry.grid(row=4, column=3, padx=15, pady=15)

        #row6
        rowIndex = rowIndex + 1
        hidden_a_for_b_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_a_for_b_circle :")
        hidden_a_for_b_circleLabel.grid(row=rowIndex, column=0, padx=15, pady=15)
        hidden_a_for_b_circleNum = tk.DoubleVar(value=0.001)
        hidden_a_for_b_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_a_for_b_circleNum)
        hidden_a_for_b_circleEntry.grid(row=rowIndex, column=1, padx=15, pady=15)

        hidden_b_for_b_circleLabel = tk.Label(tabs[tabIndex]["tab"], text="hidden_b_for_b_circle :")
        hidden_b_for_b_circleLabel.grid(row=rowIndex, column=2, padx=15, pady=15)
        hidden_b_for_b_circleNum = tk.DoubleVar(value=1000)
        hidden_b_for_b_circleEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=hidden_b_for_b_circleNum)
        hidden_b_for_b_circleEntry.grid(row=rowIndex, column=3, padx=15, pady=15)

        #Tab5
        tabIndex = tabIndex + 1
        rowIndex = 0
        numSamplesLabel = tk.Label(tabs[tabIndex]["tab"], text="num_samples : ")
        numSamplesLabel.grid(row=rowIndex, column=0, padx=0, pady=0)
        numSamplesLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=numSamplesNum)
        numSamplesLabel.grid(row=rowIndex, column=1, padx=0, pady=0)
        trainRatioLabel = tk.Label(tabs[tabIndex]["tab"], text="train_ratio : ")
        trainRatioLabel.grid(row=rowIndex, column=2, padx=0, pady=0)
        trainRatioLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=trainRatioNum)
        trainRatioLabel.grid(row=rowIndex, column=3, padx=0, pady=0)
        validRatioLabel = tk.Label(tabs[tabIndex]["tab"], text="valid_ratio : ")
        validRatioLabel.grid(row=rowIndex, column=4, padx=0, pady=0)
        validRatioLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=validRatioNum)
        validRatioLabel.grid(row=rowIndex, column=5, padx=0, pady=0)

        rowIndex = rowIndex + 1
        testRatioLabel = tk.Label(tabs[tabIndex]["tab"], text=f"test_ratio : ")
        testRatioLabel.grid(row=rowIndex, column=0, padx=0, pady=0)
        testRatioLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=testRatioNum)
        testRatioLabel.grid(row=rowIndex, column=1, padx=0, pady=0)
        selectArrayTypeLabel = tk.Label(tabs[tabIndex]["tab"], text="Array Type : ")
        selectArrayTypeLabel.grid(row=rowIndex, column=2, padx=0, pady=0)
        selectArrayTypeLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=arrayTypeValue)
        selectArrayTypeLabel.grid(row=rowIndex, column=3, padx=0, pady=0)
        numKGLabel = tk.Label(tabs[tabIndex]["tab"], text=f"num_k_g : ")
        numKGLabel.grid(row=rowIndex, column=4, padx=0, pady=0)
        numKGLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=numKGNum)
        numKGLabel.grid(row=rowIndex, column=5, padx=0, pady=0)

        rowIndex = rowIndex + 1
        NXLabel = tk.Label(tabs[tabIndex]["tab"], text="nx : ")
        NXLabel.grid(row=rowIndex, column=0, padx=0, pady=0)
        NXLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=NXNum)
        NXLabel.grid(row=rowIndex, column=1, padx=0, pady=0)
        xKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], text="x_kernel_size : ")
        xKernelSizeLabel.grid(row=rowIndex, column=2, padx=0, pady=0)
        xKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=xKernelSizeNum)
        xKernelSizeLabel.grid(row=rowIndex, column=3, padx=0, pady=0)
        NZLabel = tk.Label(tabs[tabIndex]["tab"], text="nz : ")
        NZLabel.grid(row=rowIndex, column=4, padx=0, pady=0)
        NZLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=NZNum)
        NZLabel.grid(row=rowIndex, column=5, padx=0, pady=0)

        rowIndex = rowIndex + 1
        zKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], text="z_kernel_size : ")
        zKernelSizeLabel.grid(row=rowIndex, column=0, padx=0, pady=0)
        zKernelSizeLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=zKernelSizeNum)
        zKernelSizeLabel.grid(row=rowIndex, column=1, padx=0, pady=0)
        datasetDirLabel = tk.Label(tabs[tabIndex]["tab"], text="dataset_dir : ")
        datasetDirLabel.grid(row=rowIndex, column=2, padx=0, pady=0)
        datasetDirLabel = tk.Label(tabs[tabIndex]["tab"], textvariable=datasetDirPath)
        datasetDirLabel.grid(row=rowIndex, column=3, padx=0, pady=0)
        configNameLabel = tk.Label(tabs[tabIndex]["tab"], text="configName")
        configNameLabel.grid(row=rowIndex, column=4, padx=0, pady=0)
        tempDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        configNameValue = tk.StringVar(value=tempDate)
        rootSendData = {'newConfigFileName':configNameValue, 'generateDataStop':'false'}
        configNameEntry = tk.Entry(tabs[tabIndex]["tab"], textvariable=configNameValue)
        configNameEntry.grid(row=rowIndex, column=5, padx=0, pady=0)

        import threading
        class Threader(threading.Thread):
            global sendJson
            global headers
            def __init__(self):
                print('before')
                print(rootSendData)
                global headers
                headers = {'Content-Type': 'application/json'}
                rootSendData.update({'newConfigFileName': configNameEntry.get()})
                rootSendData.update({'generateDataStop': 'false'})
                rootSendData.update({'dataset_dir': datasetDirEntry.get()})
                rootSendData.update({'num_samples': numSamplesNum.get()})
                rootSendData.update({'train_ratio': trainRatioNum.get()})
                rootSendData.update({'valid_ratio': validRatioNum.get()})
                rootSendData.update({'test_ratio': testRatioNum.get()})
                rootSendData.update({'geometry_urf': geometryUrfVar.get()})
                rootSendData.update({'Para_pkl': ParaPklVar.get()})
                rootSendData.update({'array_type': arrayTypeValue.get()})
                rootSendData.update({'num_k_g': numKGNum.get()})

                rootSendData.update({'nx': NXNum.get()})
                rootSendData.update({'nz': NZNum.get()})
                rootSendData.update({'x_kernel_size': xKernelSizeNum.get()})
                rootSendData.update({'z_kernel_size': zKernelSizeNum.get()})

                rootSendData.update({'scale_background': scaleBackgroundValue.get()})
                rootSendData.update({'pdf_background': pdfBackgroundValue.get()})
                rootSendData.update({'a_background': aBackgroundNum.get()})
                rootSendData.update({'b_background': bBackgroundNum.get()})
                rootSendData.update({'hidden_pdf_background': hiddenPdfBackgroundValue.get()})
                rootSendData.update({'use_hidden_background': useHiddenBackgroundValue.get()})
                rootSendData.update({'hidden_a_for_a_background': hidden_a_for_a_backgroundNum.get()})
                rootSendData.update({'hidden_a_for_b_background': hidden_a_for_b_backgroundNum.get()})
                rootSendData.update({'hidden_b_for_a_background': hidden_b_for_a_backgroundNum.get()})
                rootSendData.update({'hidden_b_for_b_background': hidden_b_for_b_backgroundNum.get()})

                rootSendData.update({'num_rect': num_rectNum.get()})
                w_range = [w_range_1.get(), w_range_2.get()]
                rootSendData.update({'w_range':w_range})
                h_range = [h_range_1.get(), h_range_2.get()]
                rootSendData.update({'h_range':h_range})
                rootSendData.update({'scale_rect': scale_rectValue.get()})
                rootSendData.update({'pdf_rect': pdf_rectValue.get()})
                rootSendData.update({'a_rect': a_rectNum.get()})
                rootSendData.update({'b_rect': b_rectNum.get()})
                rootSendData.update({'hidden_pdf_rect': hidden_pdf_rectValue.get()})
                rootSendData.update({'use_hidden_rect': useHiddenRectValue.get()})
                rootSendData.update({'hidden_a_for_a_rect': hidden_a_for_a_rectNum.get()})
                rootSendData.update({'hidden_b_for_a_rect': hidden_b_for_a_rectNum.get()})
                rootSendData.update({'hidden_a_for_b_rect': hidden_a_for_b_rectNum.get()})
                rootSendData.update({'hidden_b_for_b_rect': hidden_b_for_b_rectNum.get()})

                rootSendData.update({'num_circle': num_circleNum.get()})
                radius_bound = [radius_boundNum_1.get(),radius_boundNum_2.get()]
                rootSendData.update({'radius_bound':radius_bound})
                rootSendData.update({'scale_circle': scale_circleValue.get()})
                rootSendData.update({'pdf_circle': pdf_circleValue.get()})
                rootSendData.update({'a_circle': a_circleNum.get()})
                rootSendData.update({'b_circle': b_circleNum.get()})
                rootSendData.update({'hidden_pdf_circle': hidden_pdf_circleValue.get()})
                rootSendData.update({'use_hidden_circle': useHiddencircleValue.get()})
                rootSendData.update({'hidden_a_for_a_circle': hidden_a_for_a_circleNum.get()})
                rootSendData.update({'hidden_b_for_a_circle': hidden_b_for_a_circleNum.get()})
                rootSendData.update({'hidden_a_for_b_circle': hidden_a_for_b_circleNum.get()})
                rootSendData.update({'hidden_b_for_b_circle': hidden_b_for_b_circleNum.get()})
                global sendJson
                sendJson = json.dumps(rootSendData)
                print('send')
                threading.Thread.__init__(self)
                self.daemon = True
                windowParameterSet.destroy()
                self.start()

            def run(self):
                global sendJson
                global headers
                r = requests.post(f'{serverURL}/generateData', headers= headers, data=sendJson)


            btnSend = tk.Button(tabs[tabIndex]["tab"], text='傳送參數並生成資料', command =lambda:Threader())
            btnSend.grid(row=rowIndex, column=6, padx=0, pady=0)
            reLoadView(self)

        def loadDataRefreshView():
            global rootSendData
            global datasetDirPath
            global numSamplesNum
            global trainRatioNum
            global validRatioNum
            global testRatioNum
            global geometryUrfVar
            global ParaPklVar
            global arrayTypeValue
            global numKGNum

            global NXNum
            global NZNum
            global xKernelSizeNum
            global zKernelSizeNum

            global scaleBackgroundValue
            global pdfBackgroundValue
            global aBackgroundNum
            global bBackgroundNum
            global hiddenPdfBackgroundValue
            global useHiddenBackgroundValue
            global hidden_a_for_a_backgroundNum
            global hidden_a_for_b_backgroundNum
            global hidden_b_for_a_backgroundNum
            global hidden_b_for_b_backgroundNum

            global num_rectNum
            global w_range_1
            global w_range_2
            global h_range_1
            global h_range_2
            global scale_rectValue
            global pdf_rectValue
            global a_rectNum
            global b_rectNum
            global hidden_pdf_rectValue
            global useHiddenRectValue
            global hidden_a_for_a_rectNum
            global hidden_b_for_a_rectNum
            global hidden_a_for_b_rectNum
            global hidden_b_for_b_rectNum

            global num_circleNum
            global radius_boundNum_1
            global radius_boundNum_2
            global scale_circleValue
            global pdf_circleValue
            global a_circleNum
            global b_circleNum
            global hidden_pdf_circleValue
            global useHiddencircleValue
            global hidden_a_for_a_circleNum
            global hidden_b_for_a_circleNum
            global hidden_a_for_b_circleNum
            global hidden_b_for_b_circleNum
            global configNameValue

            datasetDirPath.set(rootSendData['dataset_dir'])
            numSamplesNum.set(rootSendData['num_samples'])
            trainRatioNum.set(rootSendData['train_ratio'])
            validRatioNum.set(rootSendData['valid_ratio'])
            testRatioNum.set(rootSendData['test_ratio'])
            geometryUrfVar.set(rootSendData['geometry_urf'])
            ParaPklVar.set(rootSendData['Para_pkl'])
            arrayTypeValue.set(rootSendData['array_type'])
            numKGNum.set(rootSendData['num_k_g'])

            NXNum.set(rootSendData['nx'])
            NZNum.set(rootSendData['nz'])
            xKernelSizeNum.set(rootSendData['x_kernel_size'])
            zKernelSizeNum.set(rootSendData['z_kernel_size'])

            scaleBackgroundValue.set(rootSendData['scale_background'])
            pdfBackgroundValue.set(rootSendData['pdf_background'])
            aBackgroundNum.set(rootSendData['a_background'])
            bBackgroundNum.set(rootSendData['b_background'])
            hiddenPdfBackgroundValue.set(rootSendData['hidden_pdf_background'])
            useHiddenBackgroundValue.set(rootSendData['use_hidden_background'])
            hidden_a_for_a_backgroundNum.set(rootSendData['hidden_a_for_a_background'])
            hidden_a_for_b_backgroundNum.set(rootSendData['hidden_a_for_b_background'])
            hidden_b_for_a_backgroundNum.set(rootSendData['hidden_b_for_a_background'])
            hidden_b_for_b_backgroundNum.set(rootSendData['hidden_b_for_b_background'])

            num_rectNum.set(rootSendData['num_rect'])
            w_range_1.set(rootSendData['w_range'][0])
            w_range_2.set(rootSendData['w_range'][1])
            h_range_1.set(rootSendData['h_range'][0])
            h_range_2.set(rootSendData['h_range'][1])
            scale_rectValue.set(rootSendData['scale_rect'])
            pdf_rectValue.set(rootSendData['pdf_rect'])
            a_rectNum.set(rootSendData['a_rect'])
            b_rectNum.set(rootSendData['b_rect'])
            hidden_pdf_rectValue.set(rootSendData['hidden_pdf_rect'])
            useHiddenRectValue.set(rootSendData['use_hidden_rect'])
            hidden_a_for_a_rectNum.set(rootSendData['hidden_a_for_a_rect'])
            hidden_b_for_a_rectNum.set(rootSendData['hidden_b_for_a_rect'])
            hidden_a_for_b_rectNum.set(rootSendData['hidden_a_for_b_rect'])
            hidden_b_for_b_rectNum.set(rootSendData['hidden_b_for_b_rect'])

            num_circleNum.set(rootSendData['num_circle'])
            radius_boundNum_1.set(rootSendData['radius_bound'][0])
            radius_boundNum_2.set(rootSendData['radius_bound'][1])
            scale_circleValue.set(rootSendData['scale_circle'])
            pdf_circleValue.set(rootSendData['pdf_circle'])
            a_circleNum.set(rootSendData['a_circle'])
            b_circleNum.set(rootSendData['b_circle'])
            hidden_pdf_circleValue.set(rootSendData['hidden_pdf_circle'])
            useHiddencircleValue.set(rootSendData['use_hidden_circle'])
            hidden_a_for_a_circleNum.set(rootSendData['hidden_a_for_a_circle'])
            hidden_b_for_a_circleNum.set(rootSendData['hidden_b_for_a_circle'])
            hidden_a_for_b_circleNum.set(rootSendData['hidden_a_for_b_circle'])
            hidden_b_for_b_circleNum.set(rootSendData['hidden_b_for_b_circle'])
            reLoadView(self)

    def fun(self):
        return "Hello world."
