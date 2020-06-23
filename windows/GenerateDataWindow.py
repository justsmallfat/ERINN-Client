
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime
import os
import yaml

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

        tab1 = ttk.Frame(tab_parent)
        tab2 = ttk.Frame(tab_parent)
        tab3 = ttk.Frame(tab_parent)
        tab4 = ttk.Frame(tab_parent)
        tab5 = ttk.Frame(tab_parent)

        tab_parent.add(tab1, text="generic setting_1")
        tab_parent.add(tab2, text="generic setting_2")
        tab_parent.add(tab3, text="background")
        tab_parent.add(tab4, text="rectangle")
        tab_parent.add(tab5, text="circle")

        config_dir = os.path.join('config.yml')
        stream = open(config_dir, "r")
        yaml_data = yaml.safe_load(stream)
        global serverURL
        serverURL = f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}'

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

        #Tab1
        #row1
        def getConfigData(configName):
            global rootSendData
            tabOneSendData = {'configFileName': comboxlist.get()}
            r = requests.post(f'{serverURL}/getConfigData', data=tabOneSendData)
            print("r.text")
            print(r.text)
            rootSendData = json.loads(r.text)
            loadDataRefreshView(rootSendData)
            print('rootSendData')
            print(rootSendData)

        def creatMessageView_1():
            GenerateDataMessage_1.ParameterSetWindow(window)

        btnParameterSet = tk.Button(tab1, text='？', command=creatMessageView_1)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        selectConfigLabel = tk.Label(tab1, text="選擇設定檔:")
        selectConfigLabel.grid(row=0, column=0, padx=15, pady=15)
        comvalue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        comboxlist = ttk.Combobox(tab1, textvariable=comvalue)  # 初始化
        r = requests.post(f'{serverURL}/getConfigs')
        list = r.text
        comboxlist["values"] = list.split(',')
        comboxlist.grid(row=0, column=1, padx=15, pady=15)
        comboxlist.current(0)  # 選擇第一個
        comboxlist.bind("<<ComboboxSelected>>",getConfigData)
        # getConfigBtn = tk.Button(tab1, text='取得設定檔', command = getConfigData(comboxlist.get()))
        # getConfigBtn.grid(row=0, column=2, padx=15, pady=15)

        #row2
        datasetDirLabel = tk.Label(tab1, text="dataset_dir")
        datasetDirLabel.grid(row=1, column=0, padx=15, pady=15)
        datasetDirPath = tk.StringVar(value="../data/raw_data")
        datasetDirEntry = tk.Entry(tab1, textvariable=datasetDirPath)
        datasetDirEntry.grid(row=1, column=1, padx=15, pady=15)

        numSamplesLabel = tk.Label(tab1, text="num_samples")
        numSamplesLabel.grid(row=1, column=2, padx=15, pady=15)
        numSamplesNum = tk.StringVar(value="50")
        numSamplesEntry = tk.Entry(tab1, textvariable=numSamplesNum)
        numSamplesEntry.grid(row=1, column=3, padx=15, pady=15)

        #row3
        trainRatioLabel = tk.Label(tab1, text="train_ratio")
        trainRatioLabel.grid(row=2, column=0, padx=15, pady=15)
        trainRatioNum = tk.StringVar(value="0.8")
        trainRatioEntry = tk.Entry(tab1, textvariable=trainRatioNum)
        trainRatioEntry.grid(row=2, column=1, padx=15, pady=15)

        validRatioLabel = tk.Label(tab1, text="valid_ratio")
        validRatioLabel.grid(row=2, column=2, padx=15, pady=15)
        validRatioNum = tk.StringVar(value="0.1")
        validRatioEntry = tk.Entry(tab1, textvariable=validRatioNum)
        validRatioEntry.grid(row=2, column=3, padx=15, pady=15)

        testRatioLabel = tk.Label(tab1, text="test_ratio")
        testRatioLabel.grid(row=2, column=4, padx=15, pady=15)
        testRatioNum = tk.StringVar(value="0.1")
        testRatioEntry = tk.Entry(tab1, textvariable=testRatioNum)
        testRatioEntry.grid(row=2, column=5, padx=15, pady=15)

        #row4
        geometryUrfLabel = tk.Label(tab1, text="geometry_urf")
        geometryUrfLabel.grid(row=3, column=0, padx=15, pady=15)
        geometryUrfVar = tk.StringVar(value="../config/geo.urf")
        geometryUrfEntry = tk.Entry(tab1, textvariable=geometryUrfVar)
        geometryUrfEntry.grid(row=3, column=1, padx=15, pady=15)

        ParaPklLabel = tk.Label(tab1, text="Para_pkl")
        ParaPklLabel.grid(row=3, column=2, padx=15, pady=15)
        ParaPklVar = tk.StringVar(value="../config/Para.pkl")
        ParaPklEntry = tk.Entry(tab1, textvariable=ParaPklVar)
        ParaPklEntry.grid(row=3, column=3, padx=15, pady=15)

        #row5
        selectArrayTypeLabel = tk.Label(tab1, text="選擇 Array Type")
        selectArrayTypeLabel.grid(row=4, column=0, padx=15, pady=15)
        arrayTypeValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        arrayTypeBoxList = ttk.Combobox(tab1, textvariable=arrayTypeValue)  # 初始化
        arrayTypeBoxList["values"] = ["all_combination", "Wenner"]
        arrayTypeBoxList.grid(row=4, column=1, padx=15, pady=15)
        arrayTypeBoxList.current(0)  # 選擇第一個

        numKGLabel = tk.Label(tab1, text="num_k_g")
        numKGLabel.grid(row=4, column=2, padx=15, pady=15)
        numKGNum = tk.StringVar(value="4")
        numKGEntry = tk.Entry(tab1, textvariable=numKGNum)
        numKGEntry.grid(row=4, column=3, padx=15, pady=15)


        #Tab2
        def creatMessageView_2():
            GenerateDataMessage_2.ParameterSetWindow(window)
        def creatMessageView_3():
            GenerateDataMessage_3.ParameterSetWindow(window)
        def creatMessageView_4():
            GenerateDataMessage_4.ParameterSetWindow(window)
        def creatMessageView_5():
            GenerateDataMessage_5.ParameterSetWindow(window)
        btnParameterSet = tk.Button(tab2, text='？', command=creatMessageView_2)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        frm = tk.Frame(tab2)
        frm.pack()
        frm_l = tk.Frame(frm)
        frm_r = tk.Frame(frm)
        frm_l.pack(side='left')
        frm_r.pack(side='right')

        canvas = tk.Canvas(frm_l, bg='blue', height=300, width=400)
        # image_file = tk.PhotoImage(file='sample.gif')
        # image = canvas.create_image(10, 10, anchor='ne', image=image_file)
        canvas.pack()

        zKernelSizeLabel = tk.Label(frm_r, text="z_kernel_size:")

        #row1
        NXLabel = tk.Label(frm_r, text="nx:")
        NXLabel.grid(row=0, column=0, padx=15, pady=15)
        global NXNum
        NXNum = tk.StringVar(value=140)
        NXEntry = tk.Entry(frm_r, textvariable=NXNum)
        NXEntry.grid(row=0, column=1, padx=15, pady=15)

        #row2
        NZLabel = tk.Label(frm_r, text="nz:")
        NZLabel.grid(row=1, column=0, padx=15, pady=15)
        NZNum = tk.StringVar(value="30")
        NZEntry = tk.Entry(frm_r, textvariable=NZNum)
        NZEntry.grid(row=1, column=1, padx=15, pady=15)

        #row3
        xKernelSizeLabel = tk.Label(frm_r, text="x_kernel_size:")
        xKernelSizeLabel.grid(row=2, column=0, padx=15, pady=15)
        xKernelSizeNum = tk.StringVar(value="3")
        xKernelSizeEntry = tk.Entry(frm_r, textvariable=xKernelSizeNum)
        xKernelSizeEntry.grid(row=2, column=1, padx=15, pady=15)

        #row4
        zKernelSizeLabel.grid(row=3, column=0, padx=15, pady=15)
        zKernelSizeNum = tk.StringVar(value="30")
        zKernelSizeEntry = tk.Entry(frm_r, textvariable=zKernelSizeNum)
        zKernelSizeEntry.grid(row=3, column=1, padx=15, pady=15)
        tab_parent.pack(expand=2, fill='both')

        #Tab3
        #row1
        btnParameterSet = tk.Button(tab3, text='？', command=creatMessageView_3)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        scaleBackgroundLabel = tk.Label(tab3, text="Scale background")
        scaleBackgroundLabel.grid(row=0, column=0, padx=15, pady=15)
        scaleBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scaleBackgroundBoxList = ttk.Combobox(tab3, textvariable=scaleBackgroundValue)  # 初始化
        scaleBackgroundBoxList["values"] = ["linear", "log10"]
        scaleBackgroundBoxList.grid(row=0, column=1, padx=15, pady=15)
        scaleBackgroundBoxList.current(0)  # 選擇第一個

        pdfBackgroundLabel = tk.Label(tab3, text="pdf background")
        pdfBackgroundLabel.grid(row=0, column=2, padx=15, pady=15)
        pdfBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdfBackgroundBoxList = ttk.Combobox(tab3, textvariable=pdfBackgroundValue)  # 初始化
        pdfBackgroundBoxList["values"] = ["uniform", "normal"]
        pdfBackgroundBoxList.grid(row=0, column=3, padx=15, pady=15)
        pdfBackgroundBoxList.current(0)  # 選擇第一個

        #row2
        aBackgroundLabel = tk.Label(tab3, text="a_background:")
        aBackgroundLabel.grid(row=1, column=0, padx=15, pady=15)
        aBackgroundNum = tk.StringVar(value="10")
        aBackgroundEntry = tk.Entry(tab3, textvariable=aBackgroundNum)
        aBackgroundEntry.grid(row=1, column=1, padx=15, pady=15)

        bBackgroundLabel = tk.Label(tab3, text="b_background:")
        bBackgroundLabel.grid(row=1, column=2, padx=15, pady=15)
        bBackgroundNum = tk.StringVar(value="1")
        bBackgroundEntry = tk.Entry(tab3, textvariable=bBackgroundNum)
        bBackgroundEntry.grid(row=1, column=3, padx=15, pady=15)

        #row3
        hiddenPdfBackgroundLabel = tk.Label(tab3, text="hidden_pdf_background")
        hiddenPdfBackgroundLabel.grid(row=2, column=0, padx=15, pady=15)
        hiddenPdfBackgroundValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hiddenPdfBackgroundBoxList = ttk.Combobox(tab3, textvariable=hiddenPdfBackgroundValue)  # 初始化
        hiddenPdfBackgroundBoxList["values"] = ["uniform", "normal"]
        hiddenPdfBackgroundBoxList.grid(row=2, column=1, padx=15, pady=15)
        hiddenPdfBackgroundBoxList.current(0)  # 選擇第一個

        useHiddenBackgroundValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        c1 = tk.Checkbutton(tab3, text='use_hidden_background', variable=useHiddenBackgroundValue, onvalue=1, offvalue=0)
        c1.grid(row=2, column=2, padx=15, pady=15)

        #row4
        hidden_a_for_a_backgroundLabel = tk.Label(tab3, text="hidden_a_for_a_rect:")
        hidden_a_for_a_backgroundLabel.grid(row=3, column=0, padx=15, pady=15)
        hidden_a_for_a_backgroundNum = tk.StringVar(value=0.001)
        hidden_a_for_a_backgroundEntry = tk.Entry(tab3, textvariable=hidden_a_for_a_backgroundNum)
        hidden_a_for_a_backgroundEntry.grid(row=3, column=1, padx=15, pady=15)

        hidden_b_for_a_backgroundLabel = tk.Label(tab3, text="hidden_b_for_a_rect:")
        hidden_b_for_a_backgroundLabel.grid(row=3, column=2, padx=15, pady=15)
        hidden_b_for_a_backgroundNum = tk.StringVar(value=1000)
        hidden_b_for_a_backgroundEntry = tk.Entry(tab3, textvariable=hidden_b_for_a_backgroundNum)
        hidden_b_for_a_backgroundEntry.grid(row=3, column=3, padx=15, pady=15)

        #row5
        hidden_a_for_b_backgroundLabel = tk.Label(tab3, text="hidden_a_for_a_rect:")
        hidden_a_for_b_backgroundLabel.grid(row=4, column=0, padx=15, pady=15)
        hidden_a_for_b_backgroundNum = tk.StringVar(value=0.001)
        hidden_a_for_b_backgroundEntry = tk.Entry(tab3, textvariable=hidden_a_for_b_backgroundNum)
        hidden_a_for_b_backgroundEntry.grid(row=4, column=1, padx=15, pady=15)

        hidden_b_for_b_backgroundLabel = tk.Label(tab3, text="hidden_b_for_a_rect:")
        hidden_b_for_b_backgroundLabel.grid(row=4, column=2, padx=15, pady=15)
        hidden_b_for_b_backgroundNum = tk.StringVar(value=100)
        hidden_b_for_b_backgroundEntry = tk.Entry(tab3, textvariable=hidden_b_for_b_backgroundNum)
        hidden_b_for_b_backgroundEntry.grid(row=4, column=3, padx=15, pady=15)

        #Tab4
        #row1
        btnParameterSet = tk.Button(tab4, text='？', command=creatMessageView_4)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        num_rectLabel = tk.Label(tab4, text="num_rect:")
        num_rectLabel.grid(row=0, column=0, padx=15, pady=15)
        num_rectNum = tk.StringVar(value=1)
        num_rectEntry = tk.Entry(tab4, textvariable=num_rectNum)
        num_rectEntry.grid(row=0, column=1, padx=15, pady=15)

        #row2
        w_rangeLabel = tk.Label(tab4, text="w_range :")
        w_rangeLabel.grid(row=1, column=0, padx=15, pady=15)
        w_range_1 = tk.IntVar(value=1)
        w_range_1Entry = tk.Entry(tab4, textvariable=w_range_1)
        w_range_1Entry.grid(row=1, column=1, padx=15, pady=15)
        w_range_2 = tk.IntVar(value=140)
        w_range_2Entry = tk.Entry(tab4, textvariable=w_range_2)
        w_range_2Entry.grid(row=1, column=2, padx=15, pady=15)

        #row3
        h_rangeLabel = tk.Label(tab4, text="h_range :")
        h_rangeLabel.grid(row=2, column=0, padx=15, pady=15)
        h_range_1 = tk.IntVar(value=1)
        h_range_1Entry = tk.Entry(tab4, textvariable=h_range_1)
        h_range_1Entry.grid(row=2, column=1, padx=15, pady=15)
        h_range_2 = tk.IntVar(value=30)
        h_range_2Entry = tk.Entry(tab4, textvariable=h_range_2)
        h_range_2Entry.grid(row=2, column=2, padx=15, pady=15)

        #row4
        scale_rectLabel = tk.Label(tab4, text="scale_rect")
        scale_rectLabel.grid(row=3, column=0, padx=15, pady=15)
        scale_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scale_rectBoxList = ttk.Combobox(tab4, textvariable=scale_rectValue)  # 初始化
        scale_rectBoxList["values"] = ["linear", "log10"]
        scale_rectBoxList.grid(row=3, column=1, padx=15, pady=15)
        scale_rectBoxList.current(0)  # 選擇第一個

        pdf_rectLabel = tk.Label(tab4, text="pdf_rect")
        pdf_rectLabel.grid(row=3, column=2, padx=15, pady=15)
        pdf_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdf_rectBoxList = ttk.Combobox(tab4, textvariable=pdf_rectValue)  # 初始化
        pdf_rectBoxList["values"] = ["uniform", "normal"]
        pdf_rectBoxList.grid(row=3, column=3, padx=15, pady=15)
        pdf_rectBoxList.current(0)  # 選擇第一個

        #row5
        a_rectLabel = tk.Label(tab4, text="a_rect :")
        a_rectLabel.grid(row=4, column=0, padx=15, pady=15)
        a_rectNum = tk.StringVar(value=1)
        a_rectEntry = tk.Entry(tab4, textvariable=a_rectNum)
        a_rectEntry.grid(row=4, column=1, padx=15, pady=15)

        b_rectLabel = tk.Label(tab4, text="b_rectb_rect :")
        b_rectLabel.grid(row=4, column=2, padx=15, pady=15)
        b_rectNum = tk.StringVar(value=1)
        b_rectEntry = tk.Entry(tab4, textvariable=b_rectNum)
        b_rectEntry.grid(row=4, column=3, padx=15, pady=15)

        #row6
        hidden_pdf_rectLabel = tk.Label(tab4, text="hidden_pdf_rect")
        hidden_pdf_rectLabel.grid(row=5, column=0, padx=15, pady=15)
        hidden_pdf_rectValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hidden_pdf_rectBoxList = ttk.Combobox(tab4, textvariable=hidden_pdf_rectValue)  # 初始化
        hidden_pdf_rectBoxList["values"] = ["uniform", "normal"]
        hidden_pdf_rectBoxList.grid(row=5, column=1, padx=15, pady=15)
        hidden_pdf_rectBoxList.current(0)  # 選擇第一個

        useHiddenRectValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        c2 = tk.Checkbutton(tab4, text='use_hidden_rect', variable=useHiddenRectValue, onvalue=1, offvalue=0)
        c2.grid(row=5, column=2, padx=15, pady=15)

        #row7
        hidden_a_for_a_rectLabel = tk.Label(tab4, text="hidden_a_for_a_rect :")
        hidden_a_for_a_rectLabel.grid(row=6, column=0, padx=15, pady=15)
        hidden_a_for_a_rectNum = tk.StringVar(value=0.001)
        hidden_a_for_a_rectEntry = tk.Entry(tab4, textvariable=hidden_a_for_a_rectNum)
        hidden_a_for_a_rectEntry.grid(row=6, column=1, padx=15, pady=15)

        hidden_b_for_a_rectLabel = tk.Label(tab4, text="hidden_b_for_a_rect :")
        hidden_b_for_a_rectLabel.grid(row=6, column=2, padx=15, pady=15)
        hidden_b_for_a_rectNum = tk.StringVar(value=1000)
        hidden_b_for_a_rectEntry = tk.Entry(tab4, textvariable=hidden_b_for_a_rectNum)
        hidden_b_for_a_rectEntry.grid(row=6, column=3, padx=15, pady=15)

        #row8
        hidden_a_for_b_rectLabel = tk.Label(tab4, text="hidden_a_for_b_rect :")
        hidden_a_for_b_rectLabel.grid(row=7, column=0, padx=15, pady=15)
        hidden_a_for_b_rectNum = tk.StringVar(value=0.001)
        hidden_a_for_b_rectEntry = tk.Entry(tab4, textvariable=hidden_a_for_b_rectNum)
        hidden_a_for_b_rectEntry.grid(row=7, column=1, padx=15, pady=15)

        hidden_b_for_b_rectLabel = tk.Label(tab4, text="hidden_b_for_b_rect :")
        hidden_b_for_b_rectLabel.grid(row=7, column=2, padx=15, pady=15)
        hidden_b_for_b_rectNum = tk.StringVar(value=1000)
        hidden_b_for_b_rectEntry = tk.Entry(tab4, textvariable=hidden_b_for_b_rectNum)
        hidden_b_for_b_rectEntry.grid(row=7, column=3, padx=15, pady=15)

        #Tab5
        #row1
        btnParameterSet = tk.Button(tab5, text='？', command=creatMessageView_5)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        num_circleLabel = tk.Label(tab5, text="num_circle :")
        num_circleLabel.grid(row=0, column=0, padx=15, pady=15)
        num_circleNum = tk.StringVar(value=0)
        num_circleEntry = tk.Entry(tab5, textvariable=num_circleNum)
        num_circleEntry.grid(row=0, column=1, padx=15, pady=15)

        radius_boundLabel = tk.Label(tab5, text="radius_bound :")
        radius_boundLabel.grid(row=0, column=2, padx=15, pady=15)
        radius_boundNum_1 = tk.IntVar(value=5)
        radius_bound_1Entry = tk.Entry(tab5, textvariable=radius_boundNum_1)
        radius_bound_1Entry.grid(row=0, column=3, padx=15, pady=15)
        radius_boundNum_2 = tk.IntVar(value=20)
        radius_bound_2Entry = tk.Entry(tab5, textvariable=radius_boundNum_2)
        radius_bound_2Entry.grid(row=0, column=4, padx=15, pady=15)

        #row2
        scale_circleLabel = tk.Label(tab5, text="scale_circle")
        scale_circleLabel.grid(row=1, column=0, padx=15, pady=15)
        scale_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        scale_circleBoxList = ttk.Combobox(tab5, textvariable=scale_circleValue)  # 初始化
        scale_circleBoxList["values"] = ["linear", "log10"]
        scale_circleBoxList.grid(row=1, column=1, padx=15, pady=15)
        scale_circleBoxList.current(0)  # 選擇第一個

        pdf_circleLabel = tk.Label(tab5, text="pdf_circle")
        pdf_circleLabel.grid(row=1, column=2, padx=15, pady=15)
        pdf_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        pdf_circleBoxList = ttk.Combobox(tab5, textvariable=pdf_circleValue)  # 初始化
        pdf_circleBoxList["values"] = ["uniform", "normal"]
        pdf_circleBoxList.grid(row=1, column=3, padx=15, pady=15)
        pdf_circleBoxList.current(0)  # 選擇第一個

        #row3
        a_circleLabel = tk.Label(tab5, text="a_circle :")
        a_circleLabel.grid(row=2, column=0, padx=15, pady=15)
        a_circleNum = tk.StringVar(value=1)
        a_circleEntry = tk.Entry(tab5, textvariable=a_circleNum)
        a_circleEntry.grid(row=2, column=1, padx=15, pady=15)

        b_circleLabel = tk.Label(tab5, text="b_circleb_circle :")
        b_circleLabel.grid(row=2, column=2, padx=15, pady=15)
        b_circleNum = tk.StringVar(value=1)
        b_circleEntry = tk.Entry(tab5, textvariable=b_circleNum)
        b_circleEntry.grid(row=2, column=3, padx=15, pady=15)

        #row4
        hidden_pdf_circleLabel = tk.Label(tab5, text="hidden_pdf_circle")
        hidden_pdf_circleLabel.grid(row=3, column=0, padx=15, pady=15)
        hidden_pdf_circleValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        hidden_pdf_circleBoxList = ttk.Combobox(tab5, textvariable=hidden_pdf_circleValue)  # 初始化
        hidden_pdf_circleBoxList["values"] = ["uniform", "normal"]
        hidden_pdf_circleBoxList.grid(row=3, column=1, padx=15, pady=15)
        hidden_pdf_circleBoxList.current(0)  # 選擇第一個

        useHiddencircleValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        c2 = tk.Checkbutton(tab5, text='use_hidden_circle', variable=useHiddencircleValue, onvalue=1, offvalue=0)
        c2.grid(row=3, column=2, padx=15, pady=15)

        #row5
        hidden_a_for_a_circleLabel = tk.Label(tab5, text="hidden_a_for_a_circle :")
        hidden_a_for_a_circleLabel.grid(row=4, column=0, padx=15, pady=15)
        hidden_a_for_a_circleNum = tk.StringVar(value=0.001)
        hidden_a_for_a_circleEntry = tk.Entry(tab5, textvariable=hidden_a_for_a_circleNum)
        hidden_a_for_a_circleEntry.grid(row=4, column=1, padx=15, pady=15)

        hidden_b_for_a_circleLabel = tk.Label(tab5, text="hidden_b_for_a_circle :")
        hidden_b_for_a_circleLabel.grid(row=4, column=2, padx=15, pady=15)
        hidden_b_for_a_circleNum = tk.StringVar(value=1000)
        hidden_b_for_a_circleEntry = tk.Entry(tab5, textvariable=hidden_b_for_a_circleNum)
        hidden_b_for_a_circleEntry.grid(row=4, column=3, padx=15, pady=15)

        #row6
        hidden_a_for_b_circleLabel = tk.Label(tab5, text="hidden_a_for_b_circle :")
        hidden_a_for_b_circleLabel.grid(row=5, column=0, padx=15, pady=15)
        hidden_a_for_b_circleNum = tk.StringVar(value=0.001)
        hidden_a_for_b_circleEntry = tk.Entry(tab5, textvariable=hidden_a_for_b_circleNum)
        hidden_a_for_b_circleEntry.grid(row=5, column=1, padx=15, pady=15)

        hidden_b_for_b_circleLabel = tk.Label(tab5, text="hidden_b_for_b_circle :")
        hidden_b_for_b_circleLabel.grid(row=5, column=2, padx=15, pady=15)
        hidden_b_for_b_circleNum = tk.StringVar(value=1000)
        hidden_b_for_b_circleEntry = tk.Entry(tab5, textvariable=hidden_b_for_b_circleNum)
        hidden_b_for_b_circleEntry.grid(row=5, column=3, padx=15, pady=15)

        configNameLabel = tk.Label(tab5, text="configName")
        configNameLabel.grid(row=6, column=0, padx=15, pady=15)
        tempDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # tempTime = datetime.datetime.now().time()
        configNameValue = tk.StringVar(value=tempDate)
        rootSendData = {'newConfigFileName':configNameValue, 'generateDataStop':'false'}
        configNameEntry = tk.Entry(tab5, textvariable=configNameValue)
        configNameEntry.grid(row=6, column=1, padx=15, pady=15)


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
                # print('sendJson:')
                # print(sendJson)
                r = requests.post(f'{serverURL}/generateData', headers= headers, data=sendJson)
                # windowParameterSet = tk.Toplevel(window)
                # windowParameterSet.geometry('160x90')
                # windowParameterSet.title('資料生成中')
                # selectConfigLabel = tk.Label(windowParameterSet, text="資料生成中...")
                # selectConfigLabel.grid(row=0, column=0, padx=15, pady=15)
                # windowParameterSet.destroy()


        btnSend = tk.Button(tab5, text='傳送參數並生成資料', command =lambda:Threader())
        btnSend.grid(row=6, column=2, padx=15, pady=15)



        def loadDataRefreshView(reloadData):
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

    def fun(self):
        return "Hello world."
