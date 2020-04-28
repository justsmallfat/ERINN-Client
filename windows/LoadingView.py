import asyncio

import tkinter as tk
import requests
import threading
import time
import multiprocessing as mp

# loop = asyncio.get_event_loop()
event = threading.Event()
class Window(tk.Toplevel):
    def show(self, window):
        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('160x120')
        windowParameterSet.title('資料上傳中')
        selectConfigLabel = tk.Label(windowParameterSet, text="資料上傳中...")
        selectConfigLabel.grid(row=0, column=0, padx=15, pady=15)


    def sendData(self, headers, sendJson):
        event.wait()
        requests.post('http://127.0.0.1:5000/generateData', headers= headers, data=sendJson)
        # r = loop.run_in_executor(None,requests.post('http://127.0.0.1:5000/generateData', headers= headers, data=sendJson))
        # return r

    def __init__(self, window, headers, sendJson):
        # t1 = threading.Thread(target=self.show(window))
        # t1.start()

        windowParameterSet = tk.Toplevel(window)
        windowParameterSet.geometry('160x120')
        windowParameterSet.title('資料上傳中')
        selectConfigLabel = tk.Label(windowParameterSet, text="資料上傳中...")
        selectConfigLabel.grid(row=0, column=0, padx=15, pady=15)
        time.sleep(1)
        print('MainThread set event.')
        t2 = threading.Thread(target=self.sendData(headers, sendJson))
        threading.setDaemon(True)
        t2.start()
        event.set()

        # asyncio.wait(self.sendData(headers,sendJson))
        # result = await self.sendData(headers,sendJson)
        # tasks = []
        # for i in range(1):
        #     task1 = loop.create_task(self.sendData(window, headers, sendJson))
        #     tasks.append(task1)
        #     task2 = loop.create_task(self.show(window))
        #     tasks.append(task2)
        #
        # loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()
        # asyncio.run(self.sendData(headers, sendJson))

    def fun(self):
        return "Hello world."
