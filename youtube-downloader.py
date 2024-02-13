from pytube import YouTube

#Add library pytube

# videoyt = YouTube('https://www.youtube.com/watch?v=Tm6-wufdFC0')
# print(videoyt.title)
# print(videoyt.thumbnail_url)
# print(videoyt.channel_url)

# videoyt = videoyt.streams.get_highest_resolution()
# videoyt.download()

def donwloadVideo(url):
    try:
        videoyt = YouTube(url)
        videoyt = videoyt.streams.get_highest_resolution()
        videoyt.download()
    except:
        print('not works')

# donwloadVideo('https://www.youtube.com/watch?v=Tm6-wufdFC0')
donwloadVideo('a')