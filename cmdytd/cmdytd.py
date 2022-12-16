import sys

from .shared.parser import parser
from .audio.subparser import audio_subparser
from .video.subparser import video_subparser
from .channel.subparser import channel_subparser
from .playlist.subparser import playlist_subparser


def set_default_to_help():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

def register_subparsers():
    audio_subparser()
    video_subparser()
    channel_subparser()
    playlist_subparser()

def main():
    set_default_to_help()
    register_subparsers()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
