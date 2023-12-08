from pytube import Playlist

def download_playlist(link: str = None, audio_only: bool = False):
    if link is None:
        raise ValueError
    p = Playlist(link)
    for video in p.videos:
        video.streams.first().download()
