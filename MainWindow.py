import tkinter as tk
import requests
import os
import yaml
import json
from windows import GenerateDataWindow
from windows import TrainModelWindow
from windows import PredictResistivityWindow
from windows import ShowResultWindow
from threading import Timer,Thread,Event

window = tk.Tk()
window.title('電阻預測')
window.geometry('720x540')

global rootSendData
global generateProgressName
global generateProgressValue
global trainingProgressName
global trainingProgressValue
global predictProgressName
global predictProgressValue
global timer
global intervalTime
intervalTime = 5

def parameterSet():
    GenerateDataWindow.ParameterSetWindow(window)

def trainModel():
    TrainModelWindow.ParameterSetWindow(window)

def predictResistivity():
    PredictResistivityWindow.ParameterSetWindow(window)

def showResult():
    ShowResultWindow.ParameterSetWindow(window)
    # 將資料加入 POST 請求中
    # r = requests.post('http://127.0.0.1:5000/training', data=my_data)
    # print(r.json())
def getProgressData():
    try:
        config_dir = os.path.join('config.yml')
        stream = open(config_dir, "r")
        yaml_data = yaml.safe_load(stream)
        r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/getProgress')
        global rootProgress
        rootProgress = json.loads(r.text)
        loadDataRefreshView()
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print("Timeout")
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print("TooManyRedirects")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(f'RequestException {e}')
        # raise SystemExit(e)

def loadDataRefreshView():
    global rootProgress
    try:
        if 'generateData' in rootProgress:
            generateProgressName.set(rootProgress['generateData']['name'])
            generateProgressValue.set(rootProgress['generateData']['value'])
            # print(f'generateData {generateProgressValue}')
        if 'training' in rootProgress:
            trainingProgressName.set(rootProgress['training']['name'])
            trainingProgressValue.set(rootProgress['training']['value'])
            # print(f'training: {trainingProgressValue}')
        if 'predictResistivity' in rootProgress:
            predictProgressName.set(rootProgress['predictResistivity']['name'])
            predictProgressValue.set(rootProgress['predictResistivity']['value'])
            # print(f'predictResistivity {predictProgressValue}')
    except:
        print(rootProgress)
    window.update_idletasks()
    # window.after(20000, getProgressData)


class perpetualTimer():

    def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()
    def start(self):
        self.thread.start()
    def cancel(self):
        self.thread.cancel()

def saveConfig():
    global mainWindowTimer
    mainWindowTimer.cancel()

    newConfigFilePath = os.path.join('config.yml')
    f = open(newConfigFilePath, "w")
    f.write(f"ServerDomainName : {configDomainNameEntry.get()}\n")
    f.write(f"ServerPort : {configPoartEntry.get()}\n")
    f.close()

    mainWindowTimer = perpetualTimer(intervalTime,getProgressData)
    mainWindowTimer.start()

nowRow = 0
try:
    config_dir = os.path.join('config.yml')
    stream = open(config_dir, "r")
    yaml_data = yaml.safe_load(stream)
except:
    print("ReadConfigError")


print(yaml_data['ServerDomainName'])
parameterSetMsgLabel = tk.Label(window, text="伺服器Domain")
parameterSetMsgLabel.grid(row=nowRow, column=0, columnspan=3, sticky=tk.W, padx=15, pady=15)
configDomainNameStr = tk.StringVar(value=yaml_data['ServerDomainName'])
configDomainNameEntry = tk.Entry(window, textvariable=configDomainNameStr)
configDomainNameEntry.grid(row=nowRow, column=1, padx=15, pady=15)
parameterSetMsgLabel = tk.Label(window, text="伺服器Port")
parameterSetMsgLabel.grid(row=nowRow, column=2, columnspan=3, sticky=tk.W, padx=15, pady=15)
configPoartStr = tk.StringVar(value=yaml_data['ServerPort'])
configPoartEntry = tk.Entry(window, textvariable=configPoartStr)
configPoartEntry.grid(row=nowRow, column=3, padx=15, pady=15)
btnParameterSet = tk.Button(window, text='連接', command=saveConfig)
btnParameterSet.grid(row=nowRow, column=4, padx=15, pady=15)

nowRow = nowRow+1

btnParameterSet = tk.Button(window, text='生成資料', command=parameterSet)
btnParameterSet.grid(row=nowRow, column=0, padx=15, pady=15)
parameterSetMsgLabel = tk.Label(window, text="可以讀去過往紀錄的參數，也可修正參數，並用設定的參數生成虛擬數據，以用來訓練模型。")
parameterSetMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

btnTrainModel = tk.Button(window, text='訓練模型', command=trainModel)
btnTrainModel.grid(row=nowRow, column=0, padx=15, pady=15)
trainModelMsgLabel = tk.Label(window, text="選擇之前所產數據，並設定訓練參數，以用來訓練模型。")
trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

btnTestModel = tk.Button(window, text='測試模型', command=predictResistivity)
btnTestModel.grid(row=nowRow, column=0, padx=15, pady=15)
trainModelMsgLabel = tk.Label(window, text="選擇模型，測試模型準確度。")
trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

btnTestModel = tk.Button(window, text='結果瀏覽', command=showResult)
btnTestModel.grid(row=nowRow, column=0, padx=15, pady=15)
trainModelMsgLabel = tk.Label(window, text="呈現結果，表圖下載。")
trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

parameterSetMsgLabel = tk.Label(window, text="排程")
parameterSetMsgLabel.grid(row=nowRow, column=0, padx=15, pady=15)
parameterSetMsgLabel = tk.Label(window, text="使用設定檔")
parameterSetMsgLabel.grid(row=nowRow, column=1, padx=15, pady=15)
parameterSetMsgLabel = tk.Label(window, text="進度")
parameterSetMsgLabel.grid(row=nowRow, column=2, padx=15, pady=15)

nowRow = nowRow+1

parameterSetMsgLabel = tk.Label(window, text="現在生成資料 : ")
parameterSetMsgLabel.grid(row=nowRow, column=0, sticky=tk.W, padx=15, pady=15)
generateProgressName = tk.StringVar()
parameterSetMsgLabel = tk.Label(window, textvariable=generateProgressName)
parameterSetMsgLabel.grid(row=nowRow, column=1, sticky=tk.W, padx=15, pady=15)
generateProgressValue = tk.StringVar()
parameterSetMsgLabel = tk.Label(window, textvariable=generateProgressValue)
parameterSetMsgLabel.grid(row=nowRow, column=2, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

parameterSetMsgLabel_2 = tk.Label(window, text="現在訓練模組 : ")
parameterSetMsgLabel_2.grid(row=nowRow, column=0, sticky=tk.W, padx=15, pady=15)
trainingProgressName = tk.StringVar()
parameterSetMsgLabel_2 = tk.Label(window, textvariable=trainingProgressName)
parameterSetMsgLabel_2.grid(row=nowRow, column=1, sticky=tk.W, padx=15, pady=15)
trainingProgressValue = tk.StringVar()
parameterSetMsgLabel_2 = tk.Label(window, textvariable=trainingProgressValue)
parameterSetMsgLabel_2.grid(row=nowRow, column=2, sticky=tk.W, padx=15, pady=15)

nowRow = nowRow+1

parameterSetMsgLabel_3 = tk.Label(window, text="現在測試模型 : ")
parameterSetMsgLabel_3.grid(row=nowRow, column=0, sticky=tk.W, padx=15, pady=15)
predictProgressName = tk.StringVar()
parameterSetMsgLabel_3 = tk.Label(window, textvariable=predictProgressName)
parameterSetMsgLabel_3.grid(row=nowRow, column=1, sticky=tk.W, padx=15, pady=15)
predictProgressValue = tk.StringVar()
parameterSetMsgLabel_3 = tk.Label(window, textvariable=predictProgressValue)
parameterSetMsgLabel_3.grid(row=nowRow, column=2, sticky=tk.W, padx=15, pady=15)


global mainWindowTimer
mainWindowTimer = perpetualTimer(intervalTime,getProgressData)
mainWindowTimer.start()
# window.after(500, getProgressData)

# btnPredict = tk.Button(window, text='進行預測', command=parameterSet)
# btnPredict.grid(row=3, column=0, padx=15, pady=15)
# trainModelMsgLabel = tk.Label(window, text="選擇模型，進行預測。")
# trainModelMsgLabel.grid(row=3, column=1, sticky=tk.W, padx=15, pady=15)



window.mainloop()
