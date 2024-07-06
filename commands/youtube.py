import os
import click
from pytube import YouTube

def find_paths():
    parentdir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(parentdir, "random/youtube_videos")
    os.makedirs(save_path, exist_ok=True)
    return save_path

SAVE_PATH = find_paths()

@click.group()
def youtube():
    """This script will download YouTube videos"""
    pass

@click.command()
@click.argument("url")
def download_video(url):
    """Function to download video from YouTube"""
    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"Connection error: {e}")
        return

    # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4')

    # Get the video with the highest resolution
    d_video = mp4_streams.get_highest_resolution()

    try:
        # Downloading the video
        d_video.download(output_path=SAVE_PATH)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"Errors: {e}")

youtube.add_command(download_video)
