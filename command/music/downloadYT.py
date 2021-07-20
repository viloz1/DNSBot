import youtube_dl
import os
from command.music.helpers import updateEntry

ydl_opts_global = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
        'preferredquality': '192',
    }],
    'outtmpl': 'temp/%(id)s.%(ext)s'
}

async def download(url, env):
    with youtube_dl.YoutubeDL(ydl_opts_global) as ydl:
        file = ydl.extract_info(url, download=False)
    files = os.listdir("temp")
    info = dict()
    info['id'] = str(file['id'])
    info['path'] = "temp/" + info['id'] + ".opus"
    info['title'] = str(file['title'])
    if file['id'] + ".opus" in files:
        return info
    with youtube_dl.YoutubeDL(ydl_opts_global) as ydl:
        file = ydl.extract_info(url, download=True)
    updateEntry(info['id'], env)
    return info


