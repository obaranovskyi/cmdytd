import uuid
import os
import moviepy.editor as mp
from ..shared.logger import info, error
from ..download.core import temp_download_video_using_url
from ..download.consts import youtube_url

def download_audio(video_id):
    temp_video_name = f"temp-{uuid.uuid4()}.mp4"
    video_name = temp_download_video_using_url(f"{youtube_url}watch?v={video_id}", temp_video_name)
    convert_video_to_mp3(video_name, temp_video_name)
    remove_temp_video_file(temp_video_name)
    # TODO: Under construction
    # yt = YouTube(f"{youtube_url}watch?v={video_id}", on_progress_callback=print_download_progress)
    # audio = yt.streams.filter(only_audio=True).first()
    # base, ext = os.path.splitext(audio)
    # new_file = base + '.mp3'
    # os.rename(audio, new_file)

def convert_video_to_mp3(video_name, filename):
    try:
        info('Converting to audio ...')
        clip = mp.VideoFileClip(filename)
        new_name = video_name.replace('/', '', len(video_name))
        clip.audio.write_audiofile(f"{new_name}.mp3")
    except Exception as e:
        error(e) 

def remove_temp_video_file(filename_to_remove):
    info('Cleaning ...')
    if os.path.exists(filename_to_remove):
          os.remove(filename_to_remove) 
