from pytube import YouTube

yt = YouTube("https://www.youtube.com/playlist?list=PLIf2o5zE06JZudpf9-D7fy6fg90Y7MDVO")

yt.streams.get_audio_only().download(output_path='/home/',filename=yt.title)