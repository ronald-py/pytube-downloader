from pytube import YouTube

videoyt = YouTube('https://www.youtube.com/watch?v=Tm6-wufdFC0')
print(videoyt.title)
print(videoyt.thumbnail_url)
print(videoyt.channel_url)

# videoyt2 = YouTube('https://www.youtube.com/watch?v=Tm6-wufdFC0', use_oauth=False, allow_oauth_cache=True)
videoyt = videoyt.streams.get_highest_resolution()
videoyt.download()