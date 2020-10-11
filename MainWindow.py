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
window.title('Resistance prediction')
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
global functionMsgFrame
global versionStr
functionMsgFrame = tk.Frame(window)
intervalTime = 30
timeout = 5
CLIENT_VERSION = '1.0.0'

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
    files = {'file': open(window.filename, 'rb')}
    r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/uploadModel'
                      , files =files)
    if r.text == 'Success':
        uploadModeMessageValue.set('Upload Success!')
    else:
        uploadModeMessageValue.set('Upload Fail!')
    print(r.text)


def uploadData():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    uploadDataMessageValue.set(window.filename)
    files = {'file': open(window.filename, 'rb')}
    r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/uploadData'
                      , files =files)
    if r.text == 'Success':
        uploadDataMessageValue.set('Upload Success!')
    else:
        uploadDataMessageValue.set('Upload Fail!')
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
    try:
        r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/getServerVersion'
                              , headers = {'Content-Type': 'application/json'}
                              , timeout = timeout)
        global versionStr
        versionStr = tk.StringVar(value=f'{CLIENT_VERSION}({r.text})')
        print(r.text)
    except Exception as e:
        errorMessageText.insert(1.0,"ReadConfigError")
        print(f"ReadConfigError {e}")
    global mainWindowTimer
    mainWindowTimer.cancel()
    mainWindowTimer = perpetualTimer(intervalTime, getProgressData)
    mainWindowTimer.start()

# 讀取config檔
errorMessageText = tk.Text()
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
versionStr = tk.StringVar(value=f'{CLIENT_VERSION}()')
try:
    r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/getServerVersion'
                          , headers = {'Content-Type': 'application/json'}
                          , timeout = timeout)
    versionStr = tk.StringVar(value=f'{CLIENT_VERSION}({r.text})')
    print(r.text)
except Exception as e:
    errorMessageText.insert(1.0,"ReadConfigError")
    print(f"ReadConfigError {e}")

nowRow = 0
setFrame = tk.Frame(window)
setFrame.grid(row=nowRow, column=0, sticky=tk.W, padx=5, pady=10)
serverDomainSetLabel = tk.Label(setFrame, text="Server Domain")
serverDomainSetLabel.grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
# serverDomainSetLabel.grid(row=nowRow, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
configDomainNameStr = tk.StringVar(value=yaml_data['ServerDomainName'])
configDomainNameEntry = tk.Entry(setFrame, textvariable=configDomainNameStr)
configDomainNameEntry.grid(row=0, column=1, padx=10, pady=10)
serverPortSetLabel = tk.Label(setFrame, text="Server Port")
# serverPortSetLabel.grid(row=nowRow, column=2, columnspan=3, sticky=tk.W, padx=10, pady=10)
serverPortSetLabel.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
configPoartStr = tk.StringVar(value=yaml_data['ServerPort'])
configPoartEntry = tk.Entry(setFrame, textvariable=configPoartStr)
configPoartEntry.grid(row=1, column=1, padx=10, pady=10)
btnParameterSet = tk.Button(setFrame, text='Connect', command=saveConfig)
btnParameterSet.grid(row=1, column=2, padx=10, pady=10)

logFrame = tk.Frame(window)
logFrame.grid(row=nowRow, rowspan=6, column=1, sticky=tk.W, padx=5, pady=10)
parameterSetMsgLabel = tk.Label(logFrame, text="Log")
parameterSetMsgLabel.grid(row=0, column=0, padx=10, pady=10)
generateErrorMessageValue = tk.StringVar()
errorMessageText = tk.Text(logFrame, height=35, width=60)
errorMessageText.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

versionFrame = tk.Frame(window)
versionFrame.grid(row=nowRow, column=2, sticky=tk.W, padx=5, pady=10)
versionLabel = tk.Label(versionFrame, textvariable=versionStr, justify = 'right')
versionLabel.grid(row=0, column=0, padx=0, pady=0)


def showFunctionMessage(self, message):
    # print(f'qq {message}')
    global functionMsgFrame
    functionMsgFrame.grid_forget()
    functionMsgFrame = tk.Frame(window)
    functionMsgFrame.grid(row=3, column=0, sticky=tk.W, padx=5, pady=10)
    functionMsgValue = tk.StringVar(value=message)
    functionMsgLabel = tk.Label(functionMsgFrame, textvariable=functionMsgValue, wraplength=300, justify = 'left')
    functionMsgLabel.pack(side="top", fill="x")
nowRow = nowRow+1
mainFunctionFrame = tk.Frame(window)
mainFunctionFrame.grid(row=nowRow, column=0, sticky=tk.W, padx=5, pady=10)
btnParameterSet = tk.Button(mainFunctionFrame, text='Generate Data', command=parameterSet)
btnParameterSet.grid(row=0, column=0, padx=10, pady=10)
btnParameterSet.bind("<Enter>", lambda event:showFunctionMessage(event, 'You can read the parameters recorded in the past, you can also modify the parameters, and use the set parameters to generate virtual data to train the model.'))
btnTrainModel = tk.Button(mainFunctionFrame, text='Training Model', command=trainModel)
btnTrainModel.grid(row=0, column=1, padx=10, pady=10)
btnTrainModel.bind("<Enter>", lambda event:showFunctionMessage(event, 'Select the data produced before and set the training parameters to train the model.'))
btnTestModel = tk.Button(mainFunctionFrame, text='PredictResistivity', command=predictResistivity)
btnTestModel.grid(row=0, column=2, padx=10, pady=10)
btnTestModel.bind("<Enter>", lambda event:showFunctionMessage(event, 'Select the model and test the accuracy of the model.'))
btnResult = tk.Button(mainFunctionFrame, text='Results', command=showResult)
btnResult.grid(row=0, column=3, padx=10, pady=10)
btnResult.bind("<Enter>", lambda event:showFunctionMessage(event, 'Show the results, download the table map.'))
btnUploadModel = tk.Button(mainFunctionFrame, text='Upload Model', command=uploadModel)
btnUploadModel.grid(row=1, column=0, padx=10, pady=10)
btnUploadModel.bind("<Enter>", lambda event:showFunctionMessage(event, 'Upload the custom model.'))
uploadModeMessageValue = tk.StringVar(value='Please select upload model file')
uploadModelMsgLabel = tk.Label(mainFunctionFrame, textvariable=uploadModeMessageValue)
uploadModelMsgLabel.grid(row=1, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
btnUploadData = tk.Button(mainFunctionFrame, text='Upload Data', command=uploadData)
btnUploadData.grid(row=2, column=0, padx=10, pady=10)
btnUploadData.bind("<Enter>", lambda event:showFunctionMessage(event, 'Upload real data.'))
uploadDataMessageValue = tk.StringVar(value='Please select upload data file')
uploadModelMsgLabel = tk.Label(mainFunctionFrame, textvariable=uploadDataMessageValue)
uploadModelMsgLabel.grid(row=2, column=1, columnspan=3, sticky=tk.W, padx=10, pady=10)
#
#
nowRow = 4+1
progressFrame = tk.Frame(window)
progressFrame.grid(row=nowRow, column=0, sticky=tk.W, padx=5, pady=10)
#
parameterSetMsgLabel = tk.Label(progressFrame, text="Action")
parameterSetMsgLabel.grid(row=0, column=0, padx=10, pady=10)
parameterSetMsgLabel = tk.Label(progressFrame, text="Use Config Name")
parameterSetMsgLabel.grid(row=0, column=1, padx=10, pady=10)
parameterSetMsgLabel = tk.Label(progressFrame, text="Progress")
parameterSetMsgLabel.grid(row=0, column=2, padx=10, pady=10)
# parameterSetMsgLabel = tk.Label(progressFrame, text="備註")
# parameterSetMsgLabel.grid(row=nowRow, column=3, padx=10, pady=10)
#
nowRow = nowRow+1
#
parameterSetMsgLabel = tk.Label(progressFrame, text="Generate data now : ")
parameterSetMsgLabel.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
generateProgressName = tk.StringVar()
parameterSetMsgLabel = tk.Label(progressFrame, textvariable=generateProgressName)
parameterSetMsgLabel.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)
generateProgressValue = tk.StringVar()
parameterSetMsgLabel = tk.Label(progressFrame, textvariable=generateProgressValue)
parameterSetMsgLabel.grid(row=1, column=2, sticky=tk.W, padx=10, pady=10)
btnSend = tk.Button(progressFrame, text='Stop', command =lambda:Threader('generateData',generateProgressName.get()))
btnSend.grid(row=1, column=3, padx=10, pady=10)
#
# nowRow = nowRow+1
#
parameterSetMsgLabel_2 = tk.Label(progressFrame, text="Training data now : ")
parameterSetMsgLabel_2.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
trainingProgressName = tk.StringVar()
parameterSetMsgLabel_2 = tk.Label(progressFrame, textvariable=trainingProgressName)
parameterSetMsgLabel_2.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
trainingProgressValue = tk.StringVar()
parameterSetMsgLabel_2 = tk.Label(progressFrame, textvariable=trainingProgressValue)
parameterSetMsgLabel_2.grid(row=2, column=2, sticky=tk.W, padx=10, pady=10)
btnSend = tk.Button(progressFrame, text='Stop', command =lambda:Threader('training',trainingProgressName.get()))
btnSend.grid(row=2, column=3, padx=10, pady=10)
# traininErrorMessageValue = tk.StringVar()
# errorMessageText_2 = tk.Text(window, height=1, width=80)
# errorMessageText_2.grid(row=nowRow, column=3, sticky=tk.W, padx=10, pady=10)
#
nowRow = nowRow+1
#
parameterSetMsgLabel_3 = tk.Label(progressFrame, text="Testing model now : ")
parameterSetMsgLabel_3.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
predictProgressName = tk.StringVar()
parameterSetMsgLabel_3 = tk.Label(progressFrame, textvariable=predictProgressName)
parameterSetMsgLabel_3.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
predictProgressValue = tk.StringVar()
parameterSetMsgLabel_3 = tk.Label(progressFrame, textvariable=predictProgressValue)
parameterSetMsgLabel_3.grid(row=3, column=2, sticky=tk.W, padx=10, pady=10)
btnSend = tk.Button(progressFrame, text='Stop', command =lambda:Threader('predict',predictProgressName.get()))
btnSend.grid(row=3, column=3, padx=10, pady=10)
#
# nowRow = nowRow+1
#
#
initRootProgress('waiting', 'waiting', 'waiting')
initTimmer()


window.mainloop()
