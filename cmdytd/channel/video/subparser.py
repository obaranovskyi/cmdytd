from .handler import handle
from ..shared.parser import subparsers


def video_subparser():
    video = subparsers.add_parser('video', help='Download video file from YouTube.')
    video.add_argument('video_id', type=str, help='Id of video that has to be downloaded.')
    video.set_defaults(func=handle)
