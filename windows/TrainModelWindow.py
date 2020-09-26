
from  tkinter import ttk
import tkinter as tk
import requests
import json
import datetime
import os
import yaml
from windows.message import TrainModelMessage_1
from windows.message import TrainModelMessage_2
from windows.message import TrainModelMessage_3
from windows.message import TrainModelMessage_4

class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('1000x750')
        windowParameterSet.title('Train Model')

        tab_parent = ttk.Notebook(windowParameterSet)
        tab_parent.pack(expand=2, fill='both')

        tab1 = ttk.Frame(tab_parent)
        tab2 = ttk.Frame(tab_parent)
        tab3 = ttk.Frame(tab_parent)
        tab4 = ttk.Frame(tab_parent)

        tab_parent.add(tab1, text="Preprocess")
        tab_parent.add(tab2, text="Training/Inferring_1")
        tab_parent.add(tab3, text="Training/Inferring_2")
        tab_parent.add(tab4, text="Training/Inferring_3")

        config_dir = os.path.join('config.yml')
        stream = open(config_dir, "r")
        yaml_data = yaml.safe_load(stream)
        global serverURL
        serverURL = f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}'

        global rootSendData

        global photo
        photo = tk.PhotoImage(file ='./question.gif')

        #Tab1
        #row1
        def getConfigData(configName):
            global rootSendData
            tabOneSendData = {'configFileDir': 'training', 'configFileName': selectConfigComboxlist.get()}
            r = requests.post(f'{serverURL}/getConfigData', data=tabOneSendData)
            rootSendData = json.loads(r.text)
            loadDataRefreshView(rootSendData)

        def creatMessageView_1():
            TrainModelMessage_1.ParameterSetWindow(window)
        nowRow = 0
        btnParameterSet = tk.Button(tab1, image = photo, command=creatMessageView_1)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        selectConfigLabel = tk.Label(tab1, text="Select config:")
        selectConfigLabel.grid(row=nowRow, column=0, padx=15, pady=15)
        selectConfigValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        selectConfigComboxlist = ttk.Combobox(tab1, textvariable=selectConfigValue)  # 初始化
        r = requests.post(f'{serverURL}/getTrainingConfigs')
        list = r.text
        selectConfigComboxlist["values"] = list.split(',')
        selectConfigComboxlist.grid(row=nowRow, column=1, padx=15, pady=15)
        selectConfigComboxlist.current(0)  # 選擇第一個
        selectConfigComboxlist.bind("<<ComboboxSelected>>",getConfigData)

        selectDataLabel = tk.Label(tab1, text="Select training datas:")
        selectDataLabel.grid(row=nowRow, column=2, padx=15, pady=15)
        selectDataValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        selectDatalist = ttk.Combobox(tab1, textvariable=selectDataValue)  # 初始化
        r = requests.post(f'{serverURL}/getTrainingDataList')
        list = r.text
        selectDatalist["values"] = list.split(',')
        selectDatalist.grid(row=nowRow, column=3, padx=15, pady=15)
        selectDatalist.current(0)  # 選擇第一個

        nowRow = nowRow+1
        preprocess_generatorLabel = tk.Label(tab1, text="preprocess_generator")
        preprocess_generatorLabel.grid(row=nowRow, column=0, columnspan=6, padx=15, pady=15, sticky=tk.W)

        nowRow = nowRow+1
        #row2
        preprocess_generator_add_noiseLabel = tk.Label(tab1, text="add_noise")
        preprocess_generator_add_noiseLabel.grid(row=nowRow, column=0, columnspan=2, padx=15, pady=15)
        preprocess_generator_log_transformLabel = tk.Label(tab1, text="log_transform")
        preprocess_generator_log_transformLabel.grid(row=nowRow, column=2, columnspan=4, padx=15, pady=15)

        nowRow = nowRow+1
        #row3
        preprocess_generator_add_noise_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        preprocess_generator_c1 = tk.Checkbutton(tab1, text='perform', variable=preprocess_generator_add_noise_performValue, onvalue=1, offvalue=0)
        preprocess_generator_c1.grid(row=nowRow, column=0, padx=15, pady=15)
        preprocess_generator_kwargsLabel = tk.Label(tab1, text="kwargs")
        preprocess_generator_kwargsLabel.grid(row=nowRow, column=1, padx=15, pady=15)
        preprocess_generator_log_transform_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        preprocess_generator_c2 = tk.Checkbutton(tab1, text='perform', variable=preprocess_generator_log_transform_performValue, onvalue=1, offvalue=0)
        preprocess_generator_c2.grid(row=nowRow, column=2, padx=15, pady=15)
        preprocess_generator_kwargsLabel = tk.Label(tab1, text="kwargs")
        preprocess_generator_kwargsLabel.grid(row=nowRow, column=3, padx=15, pady=15)

        nowRow = nowRow+1
        #row4
        preprocess_generator_selectArrayTypeLabel = tk.Label(tab1, text="ratio")
        preprocess_generator_selectArrayTypeLabel.grid(row=nowRow, column=1, padx=15, pady=15)
        preprocess_generator_log_transform_kwargs_inverseValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        preprocess_generator_c1 = tk.Checkbutton(tab1, text='inverse', variable=preprocess_generator_log_transform_kwargs_inverseValue, onvalue=True, offvalue=False)
        preprocess_generator_c1.grid(row=nowRow, column=3, padx=15, pady=15)

        nowRow = nowRow+1
        preprocess_generator_add_noise_kwargs_ratioValue = tk.IntVar(value="0.1")  # 窗體自帶的文字，新建一個值
        preprocess_generator_numKGEntry = tk.Entry(tab1, textvariable=preprocess_generator_add_noise_kwargs_ratioValue)
        preprocess_generator_numKGEntry.grid(row=nowRow, column=1, padx=15, pady=15)
        preprocess_generator_log_transform_kwargs_inplaceValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        preprocess_generator_c1 = tk.Checkbutton(tab1, text='inplace', variable=preprocess_generator_log_transform_kwargs_inplaceValue, onvalue=True, offvalue=False)
        preprocess_generator_c1.grid(row=nowRow, column=3, padx=15, pady=15)


        # #row2
        # raw_data_dirLabel = tk.Label(tab1, text="raw_data_dir")
        # raw_data_dirLabel.grid(row=1, column=0, padx=15, pady=15)
        # raw_data_dirPath = tk.StringVar(value="../data/raw_data")
        # raw_data_dirEntry = tk.Entry(tab1, textvariable=raw_data_dirPath)
        # raw_data_dirEntry.grid(row=1, column=1, padx=15, pady=15)
        #
        # processed_data_dirLabel = tk.Label(tab1, text="processed_data_dir")
        # processed_data_dirLabel.grid(row=1, column=2, padx=15, pady=15)
        # processed_data_dirPath = tk.StringVar(value="../data/processed_data")
        # processed_data_dirEntry = tk.Entry(tab1, textvariable=processed_data_dirPath)
        # processed_data_dirEntry.grid(row=1, column=3, padx=15, pady=15)
        #
        # #row3
        # preprocessLabel = tk.Label(tab1, text="preprocess")
        # preprocessLabel.grid(row=2, column=0, columnspan=6, padx=15, pady=15, sticky=tk.W)
        #
        # #row4
        # add_noiseLabel = tk.Label(tab1, text="add_noise")
        # add_noiseLabel.grid(row=3, column=0, columnspan=2, padx=15, pady=15)
        # log_transformLabel = tk.Label(tab1, text="log_transform")
        # log_transformLabel.grid(row=3, column=2, columnspan=4, padx=15, pady=15)
        #
        # #row5
        # preprocess_add_noise_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        # c1 = tk.Checkbutton(tab1, text='perform', variable=preprocess_add_noise_performValue, onvalue=1, offvalue=0)
        # c1.grid(row=4, column=0, padx=15, pady=15)
        # kwargsLabel = tk.Label(tab1, text="kwargs")
        # kwargsLabel.grid(row=4, column=1, padx=15, pady=15)
        # preprocess_log_transform_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        # c2 = tk.Checkbutton(tab1, text='perform', variable=preprocess_log_transform_performValue, onvalue=1, offvalue=0)
        # c2.grid(row=4, column=2, padx=15, pady=15)
        # kwargsLabel = tk.Label(tab1, text="kwargs")
        # kwargsLabel.grid(row=4, column=3, padx=15, pady=15)
        #
        # #row6
        # selectArrayTypeLabel = tk.Label(tab1, text="ratio")
        # selectArrayTypeLabel.grid(row=5, column=1, padx=15, pady=15)
        # preprocess_log_transform_inverseValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        # c1 = tk.Checkbutton(tab1, text='inverse', variable=preprocess_log_transform_inverseValue, onvalue=True, offvalue=False)
        # c1.grid(row=5, column=3, padx=15, pady=15)
        #
        # preprocess_log_transform_inplaceValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        # c1 = tk.Checkbutton(tab1, text='inplace', variable=preprocess_log_transform_inplaceValue, onvalue=True, offvalue=False)
        # c1.grid(row=6, column=3, padx=15, pady=15)
        # preprocess_add_noise_kwargs_ratio_Value = tk.IntVar(value="0.1")  # 窗體自帶的文字，新建一個值
        # numKGEntry = tk.Entry(tab1, textvariable=preprocess_add_noise_kwargs_ratio_Value)
        # numKGEntry.grid(row=6, column=1, padx=15, pady=15)

        #Tab2
        #row1
        def creatMessageView_2():
            TrainModelMessage_2.ParameterSetWindow(window)
        btnParameterSet = tk.Button(tab2, image = photo, command=creatMessageView_2)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        custom_NNLabel = tk.Label(tab2, text="custom_NN")
        custom_NNLabel.grid(row=0, column=0,  padx=15, pady=15)
        def setCustom_NN(configName):
            global custom_NNPath
            custom_NNPath = tk.StringVar(value=f"<module 'my_model' from '../config/{custom_NNPathValue.get()}'>")

        custom_NNPathValue = tk.StringVar(value='model.py')  # 窗體自帶的文字，新建一個值
        custom_NNPathComboxlist = ttk.Combobox(tab2, textvariable=custom_NNPathValue)  # 初始化
        r = requests.post(f'{serverURL}/getDLModels')
        list = r.text
        custom_NNPathComboxlist["values"] = list.split(',')
        custom_NNPathComboxlist.grid(row=0, column=1, padx=15, pady=15)
        custom_NNPathComboxlist.current(0)  # 選擇第一個
        custom_NNPathComboxlist.bind("<<ComboboxSelected>>",setCustom_NN)

        custom_NNPath = tk.StringVar(value=f"<module 'my_model' from '../config/{custom_NNPathValue.get()}'>")


        # custom_NNPath = tk.StringVar(value="<module 'my_model' from '../config/model.py'>")
        # custom_NNEntry = tk.Entry(tab2, textvariable=custom_NNPath)
        # custom_NNEntry.grid(row=0, column=1, sticky=tk.EW, columnspan=3, padx=5, pady=5)

        #row2
        train_dirLabel = tk.Label(tab2, text="train_dir")
        train_dirLabel.grid(row=1, column=0, padx=15, pady=15)
        train_dirPath = tk.StringVar(value="../data/noise_10/train")
        train_dirEntry = tk.Entry(tab2, textvariable=train_dirPath)
        train_dirEntry.grid(row=1, column=1, padx=15, pady=15)

        valid_dirLabel = tk.Label(tab2, text="valid_dir")
        valid_dirLabel.grid(row=1, column=2, padx=15, pady=15)
        valid_dirPath = tk.StringVar(value="../data/noise_10/valid")
        valid_dirEntry = tk.Entry(tab2, textvariable=valid_dirPath)
        valid_dirEntry.grid(row=1, column=3, padx=15, pady=15)

        #row3
        model_dirLabel = tk.Label(tab2, text="model_dir")
        model_dirLabel.grid(row=2, column=0, padx=15, pady=15)
        model_dirVar = tk.StringVar(value="../models/add_noise")
        model_dirEntry = tk.Entry(tab2, textvariable=model_dirVar)
        model_dirEntry.grid(row=2, column=1, padx=15, pady=15)

        pre_trained_weightsLabel = tk.Label(tab2, text="pre_trained_weights")
        pre_trained_weightsLabel.grid(row=2, column=2, padx=15, pady=15)
        pre_trained_weightsVar = tk.StringVar(value="")
        pre_trained_weightsEntry = tk.Entry(tab2, textvariable=pre_trained_weightsVar)
        pre_trained_weightsEntry.grid(row=2, column=3, padx=15, pady=15)


        #Tab3
        #row1
        def creatMessageView_3():
            TrainModelMessage_3.ParameterSetWindow(window)
        btnParameterSet = tk.Button(tab3, image = photo, command=creatMessageView_3)
        btnParameterSet.place(width = 50, height = 50, x = 940, y = 10, anchor = "nw")
        preprocess_generatorLabel = tk.Label(tab3, text="preprocess_generator")
        preprocess_generatorLabel.grid(row=0, column=0, columnspan=6, padx=15, pady=15, sticky=tk.W)

        # #row2
        # preprocess_generator_add_noiseLabel = tk.Label(tab3, text="add_noise")
        # preprocess_generator_add_noiseLabel.grid(row=1, column=0, columnspan=2, padx=15, pady=15)
        # preprocess_generator_log_transformLabel = tk.Label(tab3, text="log_transform")
        # preprocess_generator_log_transformLabel.grid(row=1, column=2, columnspan=4, padx=15, pady=15)
        #
        # #row3
        # preprocess_generator_add_noise_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        # preprocess_generator_c1 = tk.Checkbutton(tab3, text='perform', variable=preprocess_generator_add_noise_performValue, onvalue=1, offvalue=0)
        # preprocess_generator_c1.grid(row=2, column=0, padx=15, pady=15)
        # preprocess_generator_kwargsLabel = tk.Label(tab3, text="kwargs")
        # preprocess_generator_kwargsLabel.grid(row=2, column=1, padx=15, pady=15)
        # preprocess_generator_log_transform_performValue = tk.IntVar()  # 窗體自帶的文字，新建一個值
        # preprocess_generator_c2 = tk.Checkbutton(tab3, text='perform', variable=preprocess_generator_log_transform_performValue, onvalue=1, offvalue=0)
        # preprocess_generator_c2.grid(row=2, column=2, padx=15, pady=15)
        # preprocess_generator_kwargsLabel = tk.Label(tab3, text="kwargs")
        # preprocess_generator_kwargsLabel.grid(row=2, column=3, padx=15, pady=15)
        #
        # #row4
        # preprocess_generator_selectArrayTypeLabel = tk.Label(tab3, text="ratio")
        # preprocess_generator_selectArrayTypeLabel.grid(row=3, column=1, padx=15, pady=15)
        # preprocess_generator_log_transform_kwargs_inverseValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        # preprocess_generator_c1 = tk.Checkbutton(tab3, text='inverse', variable=preprocess_generator_log_transform_kwargs_inverseValue, onvalue=True, offvalue=False)
        # preprocess_generator_c1.grid(row=3, column=3, padx=15, pady=15)
        #
        # preprocess_generator_add_noise_kwargs_ratioValue = tk.IntVar(value="0.1")  # 窗體自帶的文字，新建一個值
        # preprocess_generator_numKGEntry = tk.Entry(tab3, textvariable=preprocess_generator_add_noise_kwargs_ratioValue)
        # preprocess_generator_numKGEntry.grid(row=4, column=1, padx=15, pady=15)
        # preprocess_generator_log_transform_kwargs_inplaceValue = tk.BooleanVar()  # 窗體自帶的文字，新建一個值
        # preprocess_generator_c1 = tk.Checkbutton(tab3, text='inplace', variable=preprocess_generator_log_transform_kwargs_inplaceValue, onvalue=True, offvalue=False)
        # preprocess_generator_c1.grid(row=4, column=3, padx=15, pady=15)


        #Tab4
        #row1
        def creatMessageView_4():
            TrainModelMessage_4.ParameterSetWindow(window)
        btnParameterSet = tk.Button(tab4, image = photo, command=creatMessageView_4)
        btnParameterSet.place(width = 40, height = 40, x = 950, y = 0, anchor = "nw")
        num_gpuLabel = tk.Label(tab4, text="num_gpu")
        num_gpuLabel.grid(row=0, column=0, padx=15, pady=15)
        num_gpuValue = tk.StringVar(value="1")  # 窗體自帶的文字，新建一個值
        num_gpuEntry = tk.Entry(tab4, textvariable=num_gpuValue)  # 初始化
        num_gpuEntry.grid(row=0, column=1, padx=15, pady=15)

        #row2
        batch_sizeLabel = tk.Label(tab4, text="batch size")
        batch_sizeLabel.grid(row=1, column=0, padx=15, pady=15)
        batch_sizeValue = tk.StringVar(value="8")  # 窗體自帶的文字，新建一個值
        batch_sizeEntry = tk.Entry(tab4, textvariable=batch_sizeValue)  # 初始化
        batch_sizeEntry.grid(row=1, column=1, padx=15, pady=15)

        #row2
        num_epochsLabel = tk.Label(tab4, text="num epochs")
        num_epochsLabel.grid(row=2, column=0, padx=15, pady=15)
        num_epochsValue = tk.StringVar(value="20")  # 窗體自帶的文字，新建一個值
        num_epochsEntry = tk.Entry(tab4, textvariable=num_epochsValue)  # 初始化
        num_epochsEntry.grid(row=2, column=1, padx=15, pady=15)

        #row2
        optimizerLabel = tk.Label(tab4, text="optimizer")
        optimizerLabel.grid(row=3, column=0, padx=15, pady=15)
        optimizerValue = tk.StringVar(value="Adam")  # 窗體自帶的文字，新建一個值
        optimizerEntry = tk.Entry(tab4, textvariable=optimizerValue)  # 初始化
        optimizerEntry.grid(row=3, column=1, padx=15, pady=15)

        #row2
        learning_rateLabel = tk.Label(tab4, text="learning rate")
        learning_rateLabel.grid(row=4, column=0, padx=15, pady=15)
        learning_rateValue = tk.StringVar(value="1e-4")  # 窗體自帶的文字，新建一個值
        learning_rateEntry = tk.Entry(tab4, textvariable=learning_rateValue)  # 初始化
        learning_rateEntry.grid(row=4, column=1, padx=15, pady=15)

        #row2
        lossLabel = tk.Label(tab4, text="loss")
        lossLabel.grid(row=5, column=0, padx=15, pady=15)
        lossValue = tk.StringVar(value="mean_squared_error")  # 窗體自帶的文字，新建一個值
        lossEntry = tk.Entry(tab4, textvariable=lossValue)  # 初始化
        lossEntry.grid(row=5, column=1, padx=15, pady=15)

        configNameLabel = tk.Label(tab4, text="configName")
        configNameLabel.grid(row=6, column=0, padx=15, pady=15)
        tempDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # tempTime = datetime.datetime.now().time()
        configNameValue = tk.StringVar(value=tempDate)
        configNameEntry = tk.Entry(tab4, textvariable=configNameValue)
        configNameEntry.grid(row=6, column=1, padx=15, pady=15)


        def loadDataRefreshView(reloadData):
            global rootSendData

            print('rootSendData')
            print(rootSendData)

            #tab1
            # raw_data_dirPath.set(rootSendData['raw_data_dir'])
            # processed_data_dirPath.set(rootSendData['processed_data_dir'])
            # preprocess_add_noise_performValue.set(rootSendData['preprocess']['add_noise']['perform'])
            # preprocess_add_noise_kwargs_ratio_Value.set(rootSendData['preprocess']['add_noise']['kwargs']['ratio'])
            # preprocess_log_transform_performValue.set(rootSendData['preprocess']['log_transform']['perform'])
            # preprocess_log_transform_inverseValue.set(rootSendData['preprocess']['log_transform']['kwargs']['inverse'])
            # preprocess_log_transform_inplaceValue.set(rootSendData['preprocess']['log_transform']['kwargs']['inplace'])

            preprocess_generator_add_noise_performValue.set(rootSendData['preprocess_generator']['add_noise']['perform'])
            preprocess_generator_add_noise_kwargs_ratioValue.set(rootSendData['preprocess_generator']['add_noise']['kwargs']['ratio'])
            preprocess_generator_log_transform_performValue.set(rootSendData['preprocess_generator']['log_transform']['perform'])
            preprocess_generator_log_transform_kwargs_inverseValue.set(rootSendData['preprocess_generator']['log_transform']['kwargs']['inverse'])
            preprocess_generator_log_transform_kwargs_inplaceValue.set(rootSendData['preprocess_generator']['log_transform']['kwargs']['inplace'])

            #tab2
            custom_NNPath.set(rootSendData['custom_NN'])
            train_dirPath.set(rootSendData['train_dir'])
            valid_dirPath.set(rootSendData['valid_dir'])
            model_dirVar.set(rootSendData['model_dir'])
            pre_trained_weightsVar.set(rootSendData['pre_trained_weights'])

            #tab3


            #tab4
            num_gpuValue.set(rootSendData['num_gpu'])
            batch_sizeValue.set(rootSendData['batch_size'])
            num_epochsValue.set(rootSendData['num_epochs'])
            optimizerValue.set(rootSendData['optimizer'])
            learning_rateValue.set(rootSendData['learning_rate'])
            lossValue.set(rootSendData['loss'])


        btnSend = tk.Button(tab4, text='Send', command =lambda:Threader())
        btnSend.grid(row=6, column=2, padx=15, pady=15)


        import threading
        class Threader(threading.Thread):
            global sendJson
            global headers
            def __init__(self):
                print('before')
                print(rootSendData)
                global headers
                headers = {'Content-Type': 'application/json'}
                global sendJson
                rootSendData.update({'newConfigFileName': configNameEntry.get()})
                rootSendData.update({'trainingStop': 'false'})
                rootSendData.update({'predictStop': 'false'})
                # rootSendData.update({'raw_data_dir': raw_data_dirEntry.get()})
                # rootSendData.update({'processed_data_dir': processed_data_dirEntry.get()})
                rootSendData.update({'dataset_dir': "../data/"+selectDatalist.get()})

                rootSendData.update(
                    {'preprocess_generator':
                         {'add_noise':{
                             'perform': preprocess_generator_add_noise_performValue.get(),
                             'kwargs': {
                                 'ratio':preprocess_generator_add_noise_kwargs_ratioValue.get()}},
                          'log_transform':{
                              'perform': preprocess_generator_log_transform_performValue.get(),
                              'kwargs': {
                                  'inverse':preprocess_generator_log_transform_kwargs_inverseValue.get(),
                                  'inplace':preprocess_generator_log_transform_kwargs_inplaceValue.get()}}
                         }
                    }
                )

                # rootSendData.update(
                #     {'preprocess':
                #          {'add_noise':{
                #              'perform': preprocess_add_noise_performValue.get(),
                #              'kwargs': {
                #                  'ratio':preprocess_add_noise_kwargs_ratio_Value.get()}},
                #           'log_transform':{
                #               'perform': preprocess_generator_log_transform_performValue.get(),
                #               'kwargs': {
                #                   'inverse':preprocess_log_transform_inverseValue.get(),
                #                   'inplace':preprocess_log_transform_inplaceValue.get()}}
                #          }
                #     }
                # )

                rootSendData.update({'custom_NN': f"<module 'my_model' from '../config/{custom_NNPathValue.get()}'>"})
                rootSendData.update({'train_dir': train_dirEntry.get()})
                rootSendData.update({'valid_dir': valid_dirEntry.get()})
                rootSendData.update({'model_dir': model_dirVar.get()})
                rootSendData.update({'pre_trained_weights': "0"})
                if pre_trained_weightsVar.get() :
                    rootSendData.update({'pre_trained_weights': ""+pre_trained_weightsVar.get()})

                rootSendData.update({'num_gpu': num_gpuValue.get()})
                rootSendData.update({'batch_size': batch_sizeValue.get()})
                rootSendData.update({'num_epochs': num_epochsValue.get()})
                rootSendData.update({'optimizer': optimizerValue.get()})
                rootSendData.update({'learning_rate': learning_rateValue.get()})
                rootSendData.update({'loss': lossValue.get()})


                sendJson = json.dumps(rootSendData)
                print('send')
                threading.Thread.__init__(self)
                self.daemon = True
                windowParameterSet.destroy()
                self.start()

            def run(self):
                global sendJson
                global headers
                print('headers:')
                print(headers)
                print('sendJson:')
                print(sendJson)
                r = requests.post(f'{serverURL}/training', headers= headers, data=sendJson)

    def preprocessfun(self):
        return "Hello world."
