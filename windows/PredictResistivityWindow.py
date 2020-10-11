
from  tkinter import ttk
import tkinter as tk
import requests
import json
import os
import yaml

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x300')
        windowParameterSet.title('PredictResistivity')

        tab_parent = ttk.Notebook(windowParameterSet)
        tab_parent.pack(expand=2, fill='both')

        tab1 = ttk.Frame(tab_parent)
        config_dir = os.path.join('config.yml')
        stream = open(config_dir, "r")
        yaml_data = yaml.safe_load(stream)
        global serverURL
        serverURL = f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}'

        tab_parent.add(tab1, text="Preprocess")

        global rootSendData
        global dataTypeValue
        dataTypeValue = tk.StringVar(value='Not yet selected')
        global selectConfigSizeValue
        selectConfigSizeValue = tk.StringVar(value='Not yet selected')
        data = {}
        data['pkl_dir_test'] = ''
        data['model_dir'] = ''

        rootSendData = json.loads('{"pkl_dir_test":"1","model_dir":"2"}')

        def getDataType(configName):
            global rootSendData
            sendData = {'dataFileDir': selectDatalist.get()}
            r = requests.post(f'{serverURL}/getDataType', data=sendData)
            print(f"requests.text : {r.text}")
            responseData = json.loads(r.text)
            print(f"getDataType : {responseData}")
            global dataTypeValue
            dataTypeValue.set(f'{responseData["dataType"]} {responseData["dataSize"]}')


        nowRow = 0
        selectDataLabel = tk.Label(tab1, text="Select test data:")
        selectDataLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        selectDataValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        selectDatalist = ttk.Combobox(tab1, textvariable=selectDataValue)  # 初始化
        r = requests.post(f'{serverURL}/getTrainingDataList')
        list = r.text
        selectDatalist["values"] = list.split(',')
        selectDatalist.grid(row=nowRow, column=1, padx=15, pady=15)
        selectDatalist.bind("<<ComboboxSelected>>", getDataType)
        # selectDatalist.current(0)  # 選擇第一個

        selectModelLabel = tk.Label(tab1, text="Select model:")
        selectModelLabel.grid(row=nowRow, column=2, padx=15, pady=15)
        selectModelValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        selectModellist = ttk.Combobox(tab1, textvariable=selectModelValue)  # 初始化
        r = requests.post(f'{serverURL}/getModelList')
        list = r.text
        selectModellist["values"] = list.split(',')
        selectModellist.grid(row=nowRow, column=3, padx=15, pady=15)
        selectModellist.current(0)  # 選擇第一個

        nowRow = nowRow+1
        dataTypeLabel = tk.Label(tab1, text="DataType : ")
        dataTypeLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        dataTypeValueLabel = tk.Label(tab1, textvariable=dataTypeValue)  # 初始化
        dataTypeValueLabel.grid(row=nowRow, column=1, padx=15, pady=15)


        nowRow = nowRow+1
        weights_dirLabel = tk.Label(tab1, text="weights_dir : ")
        weights_dirLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        weights_dirValue = tk.StringVar(value='weights')  # 窗體自帶的文字，新建一個值
        weights_dirEntry = tk.Entry(tab1, textvariable=weights_dirValue)  # 初始化
        weights_dirEntry.grid(row=nowRow, column=1, padx=15, pady=15)

        predictions_dirLabel = tk.Label(tab1, text="predictions_dir : ")
        predictions_dirLabel.grid(row=nowRow, column=2, padx=15, pady=15)
        predictions_dirValue = tk.StringVar(value='predictions')  # 窗體自帶的文字，新建一個值
        predictions_dirEntry = tk.Entry(tab1, textvariable=predictions_dirValue)  # 初始化
        predictions_dirEntry.grid(row=nowRow, column=3, padx=15, pady=15)

        nowRow = nowRow+1
        def getConfigData(configName):
            tabOneSendData = {'configFileDir': 'training','configFileName': comboxlist.get()}
            r = requests.post(f'{serverURL}/getConfigData', data=tabOneSendData)
            print(f"getConfigData : {r.text}")
            rootSendData = json.loads(r.text)
            global selectConfigSizeValue
            selectConfigSizeValue.set(f'NX : {rootSendData["nx"]} NZ : {rootSendData["nz"]}')

        selectConfigLabel = tk.Label(tab1, text="Select config:")
        selectConfigLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        comvalue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        comboxlist = ttk.Combobox(tab1, textvariable=comvalue)  # 初始化
        r = requests.post(f'{serverURL}/getTrainingConfigs')
        list = r.text
        comboxlist["values"] = list.split(',')
        comboxlist.grid(row=nowRow, column=1, padx=15, pady=15)
        comboxlist.bind("<<ComboboxSelected>>", getConfigData)
        # comboxlist.current(0)  # 選擇第一個
        selectConfigSizeLabel = tk.Label(tab1, text="Data Size:")
        selectConfigSizeLabel.grid(row=nowRow, column=2, padx=15, pady=15)
        selectConfigSizeValueLabel = tk.Label(tab1, textvariable=selectConfigSizeValue)
        selectConfigSizeValueLabel.grid(row=nowRow, column=3, padx=15, pady=15)

        nowRow = nowRow+1
        figs_dirLabel = tk.Label(tab1, text="figs_dir:")
        figs_dirLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        figs_dirValue = tk.StringVar(value="../reports/log_transform/testing_figs_raw")  # 窗體自帶的文字，新建一個值
        figs_dirEntry = tk.Entry(tab1, textvariable=figs_dirValue)  # 初始化
        figs_dirEntry.grid(row=nowRow, column=1, sticky=tk.W+tk.E, columnspan=2, padx=10, pady=10)

        btnSend = tk.Button(tab1, text='Send', command =lambda:Threader())
        btnSend.grid(row=nowRow, column=3, padx=5, pady=5)


        import threading
        class Threader(threading.Thread):
            global sendJson
            global headers
            def __init__(self):
                global rootSendData
                print('before')
                print(rootSendData)
                global headers
                headers = {'Content-Type': 'application/json'}
                global sendJson
                rootSendData.update({'pkl_dir_test': selectDataValue.get()})
                rootSendData.update({'model_dir': selectModelValue.get()})
                rootSendData.update({'weights_dir': weights_dirValue.get()})
                rootSendData.update({'predictions_dir': predictions_dirValue.get()})
                rootSendData.update({'newConfigFileName': comvalue.get()})
                rootSendData.update({'figs_dir':figs_dirValue.get()})
                sendJson = json.dumps(rootSendData)
                print('send')
                threading.Thread.__init__(self)
                self.daemon = True
                windowParameterSet.destroy()
                self.start()

            def run(self):
                global sendJson
                global headers
                r = requests.post(f'{serverURL}/predictResistivity', headers= headers, data=sendJson)

    def preprocessfun(self):
        return "Hello world."
