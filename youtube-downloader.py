from pytube import YouTube
from tkinter import *
import tkinter as tk
import time

#Add library pytube

def donwloadVideo(url):
    try:
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        video.download()
    except:
        print('not works')

def example():
    donwloadVideo('https://www.youtube.com/watch?v=Tm6-wufdFC0')    ## correcto
    # donwloadVideo('a')                                            ## incorrecto

def getTextInput():
    result = textExample.get("1.0", "end")
    print(result)
    return result

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x240")
    textExample = tk.Text(root, height=10)
    textExample.pack()

    btnRead = tk.Button(root, height=1, width=10, text="Read", command=getTextInput)
    btnRead.pack()

    root.mainloop()
    result = textExample.get("1.0", "end")

    donwloadVideo(result)