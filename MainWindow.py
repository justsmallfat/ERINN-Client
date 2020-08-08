import tkinter as tk
from tkinter import filedialog
import requests
import os
import yaml
import json
import threading

from SupportFiles import Tools
from windows import GenerateDataWindow
from windows import TrainModelWindow
from windows import PredictResistivityWindow
from windows import ShowResultWindow
from threading import Timer,Thread,Event

window = tk.Tk()
window.title('電阻預測')
window.geometry('980x540')

global rootSendData
global generateProgressName
global generateProgressValue
global trainingProgressName
global trainingProgressValue
global predictProgressName
global predictProgressValue
global timer
global intervalTime
intervalTime = 30
timeout = 5

#主功能按鍵
def parameterSet():

    GenerateDataWindow.ParameterSetWindow(window)
def trainModel():
    TrainModelWindow.ParameterSetWindow(window)
def predictResistivity():
    PredictResistivityWindow.ParameterSetWindow(window)
def showResult():
    ShowResultWindow.ParameterSetWindow(window)


def uploadModel():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    uploadModeMessageValue.set(window.filename)
    print (window.filename)
    files = {'file': open(window.filename, 'rb')}
    print (window.filename)
    print (files)
    r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/uploadModel'
                      , files =files)
    if r.text == 'Success':
        uploadModeMessageValue.set('上傳成功')
    else:
        uploadModeMessageValue.set('上傳失敗')
    print(r.text)

#停止活動
class Threader(threading.Thread):
    global sendJson
    def __init__(self, actionName, fileName):
        print(actionName)
        threading.Thread.__init__(self)
        global sendJson
        sendJson = json.dumps({'fileName':fileName, 'action':actionName})
        self.daemon = True
        self.start()
    def run(self):
        global sendJson
        print('sendJson:')
        print(sendJson)
        r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/stopProcess'
                          , headers= {'Content-Type': 'application/json'}
                          , timeout =10
                          , data=sendJson)
        getProgressData()

#取得進度，Log
def getProgressData():
    try:
        yaml_data = Tools.getConFigYaml_data('config.yml')
        sendJson = json.dumps(rootProgress["log"])
        print(f'getProgressData() {rootProgress["log"]}')
        r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/getProgress'
                          , headers = {'Content-Type': 'application/json'}
                          , timeout = timeout
                          , data=sendJson)
        loadDataRefreshView(json.loads(r.text))
    except requests.exceptions.Timeout as e:
        initRootProgress('--','Timeout', f'{e}')
        print("Timeout")
    except requests.exceptions.TooManyRedirects as e:
        initRootProgress('--','TooManyRedirects', f'{e}')
        print("TooManyRedirects")
    except requests.exceptions.RequestException as e:
        initRootProgress('--','RequestException', f'{e}')
        print(f'RequestException {e}')

#更新畫面
def loadDataRefreshView(progress):
    global rootProgress
    try:
        if 'generateData' in progress:
            generateProgressName.set(progress['generateData']['name'])
            generateProgressValue.set(progress['generateData']['value'])
        if 'training' in progress:
            trainingProgressName.set(progress['training']['name'])
            trainingProgressValue.set(progress['training']['value'])
        if 'predictResistivity' in progress:
            predictProgressName.set(progress['predictResistivity']['name'])
            predictProgressValue.set(progress['predictResistivity']['value'])
        if 'log' in progress:
            if(progress['log']['name'] ):
                errorMessageText.insert(1.0,
                                        f'{progress["log"]["name"]} {progress["log"]["value"]}\n{progress["log"]["message"]}\n')
    except:
        print(progress)
    # if hint:
    #     errorMessageText.insert(1.0, hint+'\n')

    window.update_idletasks()

#初始化資料
def initRootProgress(name, value, message):
    global rootProgress
    rootProgress = {}
    rootProgress['generateData'] = {'name':name,'value':value, 'message':message}
    rootProgress['training'] = {'name':name,'value':value, 'message':message}
    rootProgress['predictResistivity'] = {'name':name,'value':value, 'message':message}
    rootProgress['log'] = {'name':'','value':'', 'message':''}
    loadDataRefreshView(rootProgress)

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
    newConfigFilePath = os.path.join('config.yml')
    f = open(newConfigFilePath, "w")
    f.write(f"ServerDomainName : {configDomainNameEntry.get()}\n")
    f.write(f"ServerPort : {configPoartEntry.get()}\n")
    f.close()
    initTimmer()

mainWindowTimer = perpetualTimer(intervalTime, getProgressData)
def initTimmer():
    getProgressData()
    global mainWindowTimer
    mainWindowTimer.cancel()
    mainWindowTimer = perpetualTimer(intervalTime, getProgressData)
    mainWindowTimer.start()

# 讀取config檔
errorMessageText = tk.Text(window, height=10, width=40)
try:
    yaml_data = Tools.getConFigYaml_data('config.yml')
except OSError as e:
    config_dir = os.path.join('config.yml')
    print(f"OSError {e}")
    f = open(config_dir, "w")
    f.write("ServerDomainName : 192.168.3.11\n"
            "ServerPort : 5000")
    f.close()
    stream = open(config_dir, "r")
    yaml_data = yaml.safe_load(stream)
    errorMessageText.insert(1.0,"ReadConfigError")
except Exception as e:
    errorMessageText.insert(1.0,"ReadConfigError")
    print(f"ReadConfigError {e}")


nowRow = 0
serverDomainSetLabel = tk.Label(window, text="伺服器Domain")
serverDomainSetLabel.grid(row=nowRow, column=0, sticky=tk.W, padx=5, pady=10)
# serverDomainSetLabel.grid(row=nowRow, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
configDomainNameStr = tk.StringVar(value=yaml_data['ServerDomainName'])
configDomainNameEntry = tk.Entry(window, textvariable=configDomainNameStr)
configDomainNameEntry.grid(row=nowRow, column=1, padx=10, pady=10)
serverPortSetLabel = tk.Label(window, text="伺服器Port")
# serverPortSetLabel.grid(row=nowRow, column=2, columnspan=3, sticky=tk.W, padx=10, pady=10)
serverPortSetLabel.grid(row=nowRow, column=2, sticky=tk.W, padx=10, pady=10)
configPoartStr = tk.StringVar(value=yaml_data['ServerPort'])
configPoartEntry = tk.Entry(window, textvariable=configPoartStr)
configPoartEntry.grid(row=nowRow, column=3, padx=10, pady=10)
photo = tk.PhotoImage(file ='D:/kevin_paper/project/ERINN-Client/question.gif')
btnParameterSet = tk.Button(window, text='連接', command=saveConfig)
btnParameterSet.grid(row=nowRow, column=4, padx=10, pady=10)

# nowRow = nowRow+1
# btnParameterSet = tk.Button(window, text='生成資料', command=parameterSet)
# btnParameterSet.grid(row=nowRow, column=0, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(window, text="可以讀去過往紀錄的參數，也可修正參數，並用設定的參數生成虛擬數據，以用來訓練模型。")
# # parameterSetMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(window, text="日誌")
# parameterSetMsgLabel.grid(row=nowRow, column=4, padx=10, pady=10)
#
# nowRow = nowRow+1
# btnTrainModel = tk.Button(window, text='訓練模型', command=trainModel, )
# btnTrainModel.grid(row=nowRow, column=0, padx=10, pady=10)
# trainModelMsgLabel = tk.Label(window, text="選擇之前所產數據，並設定訓練參數，以用來訓練模型。")
# # trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
# generateErrorMessageValue = tk.StringVar()
# errorMessageText.grid(row=nowRow, rowspan=4, column=4, sticky=tk.W, padx=10, pady=10)
#
# nowRow = nowRow+1
# btnTestModel = tk.Button(window, text='測試模型', command=predictResistivity)
# btnTestModel.grid(row=nowRow, column=0, padx=10, pady=10)
# trainModelMsgLabel = tk.Label(window, text="選擇模型，測試模型準確度。")
# # trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# btnTestModel = tk.Button(window, text='結果瀏覽', command=showResult)
# btnTestModel.grid(row=nowRow, column=0, padx=10, pady=10)
# trainModelMsgLabel = tk.Label(window, text="呈現結果，表圖下載。")
# # trainModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# btnUploadModel = tk.Button(window, text='上傳模組', command=uploadModel)
# btnUploadModel.grid(row=nowRow, column=0, padx=10, pady=10)
# uploadModeMessageValue = tk.StringVar(value='請選擇上傳模組檔案')
# uploadModelMsgLabel = tk.Label(window, textvariable=uploadModeMessageValue)
# # uploadModelMsgLabel.grid(row=nowRow, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# parameterSetMsgLabel = tk.Label(window, text="排程")
# parameterSetMsgLabel.grid(row=nowRow, column=0, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(window, text="使用設定檔")
# parameterSetMsgLabel.grid(row=nowRow, column=1, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(window, text="進度")
# parameterSetMsgLabel.grid(row=nowRow, column=2, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(window, text="備註")
# parameterSetMsgLabel.grid(row=nowRow, column=3, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# parameterSetMsgLabel = tk.Label(window, text="現在生成資料 : ")
# parameterSetMsgLabel.grid(row=nowRow, column=0, sticky=tk.W, padx=10, pady=10)
# generateProgressName = tk.StringVar()
# parameterSetMsgLabel = tk.Label(window, textvariable=generateProgressName)
# parameterSetMsgLabel.grid(row=nowRow, column=1, sticky=tk.W, padx=10, pady=10)
# generateProgressValue = tk.StringVar()
# parameterSetMsgLabel = tk.Label(window, textvariable=generateProgressValue)
# parameterSetMsgLabel.grid(row=nowRow, column=2, sticky=tk.W, padx=10, pady=10)
# btnSend = tk.Button(window, text='暫停', command =lambda:Threader('generateData',generateProgressName.get()))
# btnSend.grid(row=nowRow, column=4, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# parameterSetMsgLabel_2 = tk.Label(window, text="現在訓練模組 : ")
# parameterSetMsgLabel_2.grid(row=nowRow, column=0, sticky=tk.W, padx=10, pady=10)
# trainingProgressName = tk.StringVar()
# parameterSetMsgLabel_2 = tk.Label(window, textvariable=trainingProgressName)
# parameterSetMsgLabel_2.grid(row=nowRow, column=1, sticky=tk.W, padx=10, pady=10)
# trainingProgressValue = tk.StringVar()
# parameterSetMsgLabel_2 = tk.Label(window, textvariable=trainingProgressValue)
# parameterSetMsgLabel_2.grid(row=nowRow, column=2, sticky=tk.W, padx=10, pady=10)
# btnSend = tk.Button(window, text='暫停', command =lambda:Threader('training',trainingProgressName.get()))
# btnSend.grid(row=nowRow, column=4, padx=10, pady=10)
# # traininErrorMessageValue = tk.StringVar()
# # errorMessageText_2 = tk.Text(window, height=1, width=80)
# # errorMessageText_2.grid(row=nowRow, column=3, sticky=tk.W, padx=10, pady=10)
#
# nowRow = nowRow+1
#
# parameterSetMsgLabel_3 = tk.Label(window, text="現在測試模型 : ")
# parameterSetMsgLabel_3.grid(row=nowRow, column=0, sticky=tk.W, padx=10, pady=10)
# predictProgressName = tk.StringVar()
# parameterSetMsgLabel_3 = tk.Label(window, textvariable=predictProgressName)
# parameterSetMsgLabel_3.grid(row=nowRow, column=1, sticky=tk.W, padx=10, pady=10)
# predictProgressValue = tk.StringVar()
# parameterSetMsgLabel_3 = tk.Label(window, textvariable=predictProgressValue)
# parameterSetMsgLabel_3.grid(row=nowRow, column=2, sticky=tk.W, padx=10, pady=10)
# btnSend = tk.Button(window, text='暫停', command =lambda:Threader('predict',predictProgressName.get()))
# btnSend.grid(row=nowRow, column=4, padx=10, pady=10)
#
# nowRow = nowRow+1
#
#
# initRootProgress('waiting', 'waiting', 'waiting')
# initTimmer()


window.mainloop()
