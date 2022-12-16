from .handler import handle
from ..shared.parser import subparsers


def channel_subparser():
    channel = subparsers.add_parser('channel', help='Download channel-related videos from YouTube.')
    channel.add_argument('channel_id', type=str, help='Id of channel that has to be downloaded.')
    channel.set_defaults(func=handle)
