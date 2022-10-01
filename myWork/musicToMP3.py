from youtube_search import YoutubeSearch
import time, os
from pytube import YouTube
artists = []
songs = []
youtubeLinks = []
short = ""

def collectSongs():
    global short
    text = open('INSERT FILE PATH HERE', 'r').readlines()
    for i in text:
        removed = i.removesuffix("\n")
        if removed == "":
            continue
        elif removed[0] == "-":
            if short == "-":
                break
            artists.append(removed.split("-")[1][1:])
            songs.append([])
            short = "-"
        else:
            songs[-1].append(removed.removeprefix("  "))
            short = "yes"

collectSongs()
artists.pop()
songs.pop()

def downloadMusic(link):

    # url input from user
    yt = YouTube(str(link))
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    destination = "G:\Download\Music"
    # download the file
    out_file = video.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")

def getLinks():
    for i in range(len(artists)):
        for j in songs[i]:
            try:
                results = YoutubeSearch(f'{artists[i]} - {j} lyric video', max_results=1).to_dict()
            except:
                times.sleep(120)
                results = YoutubeSearch(f'{artists[i]} - {j} lyric video', max_results=1).to_dict()
            for v in results:
                link = 'https://www.youtube.com' + v['url_suffix']
                youtubeLinks.append(link)
                print(f'Link: {link}\nSong Name: {artists[i]} - {j}')
                downloadMusic(link)
getLinks()
