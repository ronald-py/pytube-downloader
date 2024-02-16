from pytube import YouTube
from tkinter import *
import tkinter as tk
import time

#Add library pytube

def donwloadVideo():
    url = inputWindow.get()
    
    try:
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        video.download()
        time.sleep(5)
        labelMessage = tk.Label(windowTk, text="Exito al descargar!")
        labelMessage.pack()

    except:
        labelMessage = tk.Label(windowTk, text="Ocurrio un error!")
        labelMessage.pack()

def example():
    donwloadVideo('https://www.youtube.com/watch?v=Tm6-wufdFC0')    ## correcto
    donwloadVideo('a')                                              ## incorrecto

if __name__ == "__main__":
    windowTk = tk.Tk()

    inputWindow = tk.Entry(windowTk)
    inputWindow.pack(pady=10, padx=10)

    buttonDownload = tk.Button(windowTk, text="Descargar", command=donwloadVideo)
    buttonDownload.pack(padx=30, pady=30)

    windowTk.mainloop()