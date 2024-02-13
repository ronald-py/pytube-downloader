from pytube import YouTube
from tkinter import *
from tkinter import ttk

#Add library pytube

def donwloadVideo(url):
    try:
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        video.download()
    except:
        print('not works')


def main():
    donwloadVideo('https://www.youtube.com/watch?v=Tm6-wufdFC0')    ## correcto
    donwloadVideo('a')                                              ## incorrecto

if __name__ == "__main__":
    main()