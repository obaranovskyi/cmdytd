from ..download.core import download_playlist

def handle(args):
    download_playlist(args.playlist_id)
