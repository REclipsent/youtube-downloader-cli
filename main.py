import typer
from rich import print
import pytube
import shellingham
import os

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
def download(link: str, verbose: bool = True):
    print(link)
    if verbose:
        print("Downloading Link")

if __name__ == '__main__':
    app()