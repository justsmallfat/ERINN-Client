import math
from  tkinter import ttk
import tkinter as tk
import requests
import json
import io

from cffi.backend_ctypes import xrange
from urllib.request import urlopen
from PIL import Image, ImageTk


class ParameterSetWindow(tk.Toplevel):
    def __init__(self, window, url):

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0*w_box/w # 1.0 forces float division in Python2
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('800x750')
        windowParameterSet.title(url)
        print(f'ParameterSetWindow {url}')
        image_bytes = urlopen(url).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
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
        label.grid(row=0, column=0, sticky='news')

        # tab_parent.add(tab2, text="PredictResistivity/Inferring_1")


    def preprocessfun(self):
        return "Hello world."
