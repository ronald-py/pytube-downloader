from pytube import YouTube
from tkinter import ttk
import tkinter as tk
import time

#Add library pytube

def donwloadVideo():
    url = inputWindow.get()
    
    try:
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        # video = video.streams.get_audio_only()
        # video = video.streams.filter(file_extension='mp4')
        video.download()
        name = video.title
        print(name)
        time.sleep(5)
        labelMessage = tk.Label(windowTk, text="Exito al descargar!")
        labelMessage.pack()

    except:
        labelMessage = tk.Label(windowTk, text="Ocurrio un error!")
        labelMessage.pack()

def example():
    donwloadVideo('https://www.youtube.com/watch?v=Tm6-wufdFC0')    ## correcto
    donwloadVideo('a')                                              ## incorrecto

def getOptionFormat():
    option = comboFormat.get()

if __name__ == "__main__":

    optionFormat = ['mp3', 'mp4']

    windowTk = tk.Tk()
    windowTk.title ("Pydownloader")

    labelBox = tk.Label(windowTk, text="Inserte url del video:")
    labelBox.pack()

    inputWindow = tk.Entry(windowTk, width=50)
    inputWindow.pack(pady=10, padx=20)

    labelFormat = tk.Label(windowTk, text="Seleccione el formato")
    labelFormat.pack()

    comboFormat = ttk.Combobox(windowTk, values=optionFormat)
    comboFormat.bind("<<ComboboxSelected>>", getOptionFormat)
    comboFormat.pack()

    buttonDownload = tk.Button(windowTk, text="Descargar", command=donwloadVideo)
    buttonDownload.pack(pady=30)

    windowTk.mainloop()