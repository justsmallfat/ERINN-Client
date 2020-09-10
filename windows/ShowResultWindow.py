import math
from  tkinter import ttk
import tkinter as tk
from urllib import parse

import requests
import json
import io
import os
import yaml
from functools import partial

from cffi.backend_ctypes import xrange
from urllib.request import urlopen
from PIL import Image, ImageTk

from windows import ShowBigImageWindow


class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('1000x750')
        windowParameterSet.title('結果瀏覽')

        tab_parent = ttk.Notebook(windowParameterSet)
        tab_parent.pack(expand=2, fill='both')

        tab1 = ttk.Frame(tab_parent)

        config_dir = os.path.join('config.yml')
        stream = open(config_dir, "r")
        yaml_data = yaml.safe_load(stream)
        global serverURL
        serverURL = f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}'

        tab_parent.add(tab1, text="Preprocess")
        # tab_parent.add(tab2, text="PredictResistivity/Inferring_1")

        global rootSendData
        data = {}
        data['pkl_dir_test'] = ''
        data['model_dir'] = ''

        rootSendData = json.loads('{"pkl_dir_test":"1","model_dir":"2"}')

        global imageList

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0*w_box/w # 1.0 forces float division in Python2
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        def showBigPic(url, sendData):
            print(f'url {url}')
            ShowBigImageWindow.ParameterSetWindow(window, url, sendData)

        #Tab1
        #row1
        def getImagesNames(dirName):
            sendData = {'figs_dir': selectDatalist.get()}
            sendJson = json.dumps(sendData)
            print(f'sendData {sendJson}')
            r = requests.post(f'{serverURL}/getReportImgsList',
                                headers= {'Content-Type': 'application/json'},
                                data=sendJson)
            # 先拿資料
            global imageList
            imageList = r.text.split(',')
            print(len(imageList))
            print(imageList)


            if(len(imageList)<25):
                totalPageCount = 1
            else:
                totalPageCount = math.ceil(len(imageList)/25)


            if(totalPageCount<30):
                rowCount = 1
            else:
                rowCount = math.ceil(totalPageCount/30)

            pages_labels = [[tk.Button() for j in xrange(30)]
                      for i in xrange(rowCount)]
            print(f'pages_labels {pages_labels}')

            for i in range(rowCount):
                for j in range(30):
                    nowIndex = i*30+j
                    print(f'nowIndex {nowIndex} totalPageCount {totalPageCount} j {j} i {i}')
                    pages_labels[i][j] = tk.Button(frame_pages, text=f"{nowIndex+1}", command=partial(showImagesByPage, nowIndex))
                    pages_labels[i][j].grid(row=i, column=j, sticky='news')
                    frame_pages.update_idletasks()
                    first5columns_width = 750
                    first5rows_height = 100
                    frame_canvas_pages.config(width=first5columns_width + vsb_pages.winfo_width(),
                                        height=first5rows_height)
                    canvas_pages.config(scrollregion=canvas.bbox("all"))
                    # Threader(nowIndex,i,j).run()

            frame_Images.update_idletasks()
            first5columns_width = 950
            first5rows_height = 100
            frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                                height=first5rows_height)
            canvas.config(scrollregion=canvas.bbox("all"))




            frame_Images.update_idletasks()
            first5columns_width = 750
            first5rows_height = 500
            frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                                height=first5rows_height)
            canvas.config(scrollregion=canvas.bbox("all"))
            # 讀圖
            print(r.text)

        def showImagesByPage(page):
            startIndex = (page*25)+1
            pageImageCount = len(imageList) - startIndex
            if(pageImageCount < 5):
                rowCount = 1
            else:
                if(pageImageCount>25):
                    pageImageCount = 25

            rowCount = math.ceil(pageImageCount/5)

            print(f'page {page} startIndex {startIndex} rowCount {rowCount} pageImageCount {pageImageCount}')
            labels = [[tk.Button() for j in xrange(5)]
                      for i in xrange(rowCount)]
            print(len(labels))
            for i in range(rowCount):
                for j in range(5):
                    nowIndex = startIndex + (i*5+j)
                    print(f'nowIndex {nowIndex} rowCount {rowCount} j {j}')
                    if  nowIndex >= len(imageList):break
                    labels[i][j] = tk.Button(frame_Images, text=imageList[nowIndex])
                    labels[i][j].grid(row=i, column=j, sticky='news')
                    Threader(nowIndex,i,j).run()

        # selectDataLabel = tk.Label(tab1, image=tk_image, text="qq")
        selectDataLabel = tk.Label(tab1, text="Select folder:")
        selectDataLabel.grid(row=0, column=0, pady=(5, 0), sticky='nw')


        selectDataValue = tk.StringVar()  # 窗體自帶的文字，新建一個值
        selectDatalist = ttk.Combobox(tab1, textvariable=selectDataValue)  # 初始化
        r = requests.post(f'{serverURL}/getReportsList')
        list = r.text
        selectDatalist["values"] = list.split(',')
        selectDatalist.grid(row=0, column=1, pady=(5, 0), sticky='nw')
        selectDatalist.current(0)  # 選擇第一個
        selectDatalist.bind("<<ComboboxSelected>>",getImagesNames)


        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(tab1)
        frame_canvas.grid(row=1, column=0, columnspan=2, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        frame_Images = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_Images, anchor='nw')

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))




        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas_pages = tk.Frame(tab1)
        frame_canvas_pages.grid(row=2, column=0, columnspan=2, pady=(5, 0), sticky='nw')
        frame_canvas_pages.grid_rowconfigure(0, weight=1)
        frame_canvas_pages.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas_pages.grid_propagate(False)

        # Add a canvas in that frame
        canvas_pages = tk.Canvas(frame_canvas_pages)
        canvas_pages.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb_pages = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb_pages.grid(row=0, column=1, sticky='ns')
        canvas_pages.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        frame_pages = tk.Frame(canvas_pages)
        canvas_pages.create_window((0, 0), window=frame_pages, anchor='nw')

        # Set the canvas scrolling region
        canvas_pages.config(scrollregion=canvas.bbox("all"))


        import threading
        class Threader(threading.Thread):
            global sendJson, rootNowIndex, rootI, rootJ
            def __init__(self, nowIndex, i, j):
                global sendJson, rootNowIndex, rootI, rootJ
                rootNowIndex = nowIndex
                rootI = i
                rootJ = j
                print('send')
                threading.Thread.__init__(self)
                self.daemon = True
                self.start()

            def run(self):
                global sendJson, rootNowIndex, rootI, rootJ
                rowCount = math.ceil(len(imageList)/5)
                labels = [[tk.Button() for j in xrange(5)] for i in xrange(rowCount)]
                print(rootNowIndex)
                print(imageList[rootNowIndex])
                if  rootNowIndex >= len(imageList):return
                url = f"{serverURL}/uploads/{imageList[rootNowIndex]}"
                sendData = {'figs_dir': selectDatalist.get()}
                data = parse.urlencode(sendData).encode()
                # print(f'sendData {sendJson}')
                headers= {'Content-Type': 'application/json'}
                image_bytes = urlopen(url,
                                      data=data).read()
                # internal data file
                data_stream = io.BytesIO(image_bytes)
                # open as a PIL image object
                pil_image = Image.open(data_stream)
                # put the image on a typical widget

                w, h = pil_image.size

                # resize the image so it retains its aspect ration
                # but fits into the specified display box
                #缩放图像让它保持比例，同时限制在一个矩形框范围内
                pil_image_resized = resize(w, h, 200, 100, pil_image)
                tk_image = ImageTk.PhotoImage(pil_image_resized)

                labels[rootI][rootJ] = tk.Button(frame_Images,
                                                 image=tk_image,
                                                 text=imageList[rootNowIndex],
                                                 command=lambda:showBigPic(url, sendData))
                labels[rootI][rootJ].image = tk_image
                labels[rootI][rootJ].grid(row=rootI, column=rootJ, sticky='news')

                frame_Images.update_idletasks()
                first5columns_width = 750
                first5rows_height = 500
                # first5columns_width = sum([labels[0][rootJ].winfo_width() for j in range(0, 5)])
                # first5rows_height = sum([labels[rootI][0].winfo_height() for i in range(0, 5)])
                frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                                    height=first5rows_height)

                canvas.config(scrollregion=canvas.bbox("all"))

    def preprocessfun(self):
        return "Hello world."
