from pytube import Playlist
from pytube import YouTube

def get_playlist(playlists):
    urls=[]
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)


    return urls


playlist = ['PLAYLIST URL']
pl_urls = get_playlist(playlist)

#print(pl_urls)


for urld in pl_urls:
    yt = YouTube(urld)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_369p_files = mp4_files.get_by_resolution("720p")
    mp4_369p_files.download("OUTPUT DESTINATION FOLDER")
