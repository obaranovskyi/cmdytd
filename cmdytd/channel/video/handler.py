from ..download.core import download_video_using_url

def handle(args):
    download_video_using_url(args.video_id)
