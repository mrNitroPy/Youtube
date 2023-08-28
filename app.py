# -*- coding: utf-8 -*-

from pytube import YouTube, Playlist
import re
import os

play = 'http://www.youtube.com/watch?v=S8ZpQDZui9Q' # one video download
# play = 'https://youtube.com/playlist?list=PLAt10Vana3YeAwS_LyLCeu7chml8eP8bh&si=aae8E6fKbVtiRonW' # playlist download

play_list = False
if re.search(r"https:\/\/(?:www\.)?youtube.com/playlist\?list=(.*)", play):
    video_url = Playlist(play)
    play_list = True
else:
    video_url = YouTube(play)
    play_list = False

path_dir = os.path.exists('downloads')
if not path_dir:
    print('Created folder downloade')
    os.mkdir('downloads')





if play_list:
    dls= 1
    print('Start Downloading PlayList...')
    for i, url in enumerate(video_url):
        yt = YouTube(url)
        title = yt.title
        yt.streams.get_by_itag(22).download('downloads')
        print (f"End Download video number = {dls}", '')
        dls +=1
else:
    stream = video_url.streams
    chars = ""
    for x in stream.filter(file_extension='mp4'):
        chars += f"resulation {x.resolution} | download send code = {x.itag}\n\n"

    print(chars, ' ')
    get_itag = input('send code with download video: ')

    if get_itag:
        try:
            print('start download...')
            stream.get_by_itag(get_itag).download('downloads')
        except Exception as e:
            print(f'crash download {str(e)}')
    else:
        get_itag = input('pleas is not empty send code with download video: ')