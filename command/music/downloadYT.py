import youtube_dl

ydl_opts_global = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
        'preferredquality': '192',
    }],
    'outtmpl': 'temp/%(id)s.%(ext)s'
}

async def download(url):
    with youtube_dl.YoutubeDL(ydl_opts_global) as ydl:
        file = ydl.extract_info(url, download=True)
    path = "temp/" + str(file['id'] + ".opus")
    title = str(file['title'])
    return [path,title]


