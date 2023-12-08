import typer
from rich import print
from pytube import YouTube, Playlist
import shellingham
import os
from utils import verb_print, download_playlist

def provide_default():
    if os.name == 'posix':
        return os.environ['SHELL']
    elif os.name == 'nt':
        return os.environ['COMSPEC']
    raise NotImplementedError(f'OS {os.name!r} support not available')

try:
    shell = shellingham.detect_shell()
except shellingham.ShellDetectionFailure:
    shell = provide_default()

app = typer.Typer()

@app.command()
def download(link: str, audio_only: bool = False, verbose: bool = False):
    print(link)
    if 'watch' in link:
        print('Is video')
    elif 'playlist' in link:
        verb_print('Detected Playlist Link', verbose)
        download_playlist(link, audio_only)

    verb_print('Downloading Link', verbose)

if __name__ == '__main__':
    app()