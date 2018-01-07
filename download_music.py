from __future__ import unicode_literals
import youtube_dl
import sys


music = sys.argv[1]

ydl_pts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_pts) as ydl:
    ydl.download([str(music)])
