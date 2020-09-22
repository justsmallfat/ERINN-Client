import tkinter as tk
from urllib import parse

import requests
import json
import io

from cffi.backend_ctypes import xrange
from urllib.request import urlopen
from PIL import Image, ImageTk
from tkinter import filedialog


class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window, url, sendData):
        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0*w_box/w # 1.0 forces float division in Python2
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x700')
        windowParameterSet.title(url)
        print(f'ParameterSetWindow {url}')
        data = parse.urlencode(sendData).encode()
        image_bytes = urlopen(url,
                              data=data).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
        global pil_image
        pil_image = Image.open(data_stream)
        # put the image on a typical widget

        w, h = pil_image.size

        # resize the image so it retains its aspect ration
        # but fits into the specified display box
        #缩放图像让它保持比例，同时限制在一个矩形框范围内
        pil_image_resized = resize(w, h, 800, 600, pil_image)
        tk_image = ImageTk.PhotoImage(pil_image_resized)

        label = tk.Label(windowParameterSet, image=tk_image, text="qq")
        label.image = tk_image
        label.grid(row=0, column=0, rowspan=8, sticky='news')



        def downloadImage():
            name = url.rsplit('/', 1)[1]
            print(name)
            window.filename =  filedialog.asksaveasfilename(initialfile = f"{name}",title = "Select file", defaultextension = '.png' , filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
            downloadImageMessageValue.set(window.filename)
            global pil_image
            print(pil_image)
            pil_image.save(f'{window.filename}.png', "PNG")
            # files = {'file': open(window.filename, 'rb')}
            # r = requests.post(f'http://{yaml_data["ServerDomainName"]}:{yaml_data["ServerPort"]}/uploadModel'
            #                   , files =files)
            # if r.text == 'Success':
            #     downloadImageMessageValue.set('Upload Success!')
            # else:
            #     downloadImageMessageValue.set('Upload Fail!')
            # print(r.text)

        btnDownloadImage = tk.Button(windowParameterSet, text='Download Image', command=downloadImage)
        btnDownloadImage.grid(row=0, column=1, padx=10, pady=10)
        # btnUploadModel.bind("<Enter>", lambda event:showFunctionMessage(event, 'Download the Images.'))
        downloadImageMessageValue = tk.StringVar(value='Please select dir')
        # downloadImageLabel = tk.Label(windowParameterSet, textvariable=downloadImageMessageValue)
        # downloadImageLabel.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)


    def preprocessfun(self):
        return "Hello world."
