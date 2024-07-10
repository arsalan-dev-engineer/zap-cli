from pathlib import Path
import yt_dlp
import os

def setup_paths():
    """
    Setup the parent directory path for video downloads.
    Returns:
        Path object for the parent directory.
    """
    # Get the current directory of the script
    currentdir = Path(__file__).resolve().parent
    # Get the parent directory of the current directory
    parentdir = currentdir.parent
    # Return the path to the parent directory
    return parentdir

def download_youtube_video(parentdir):
    """
    Download a YouTube video to the specified parent directory.
    Args:
        parentdir (Path): The parent directory where the video will be saved.
    """
    # Define the path for saving the video
    file_path = os.path.join(parentdir, "misc/youtube_videos/")
    # Check if the directory does not exist
    if not os.path.exists(file_path):
        # Create the directory if it does not exist
        os.makedirs(file_path)

    # Define the options for yt_dlp to download the video
    ydl_opts = {
        # Request the best available video and audio formats
        'format': 'bestvideo+bestaudio/best',
        # Set the output path and filename template
        'outtmpl': os.path.join(file_path, '%(title)s.%(ext)s'),
        # Merge video and audio into mp4 format
        'merge_output_format': 'mp4',
        # Download only the single video, not a playlist
        'noplaylist': True,
        # Add a progress hook to monitor download progress
        'progress_hooks': [hook_function],
        # Remove the cache directory after the download
        'rm_cache_dir': True,
        # Specify the path to ffmpeg executable
        'ffmpeg_location': '/usr/bin/ffmpeg',
        'postprocessors': [{
            # Postprocess the video to convert it to the desired format
            'key': 'FFmpegVideoConvertor',
            # Set the preferred output format to MP4
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': [
            # Use x264 for video encoding
            '-c:v', 'libx264',
            # Use AAC for audio encoding
            '-c:a', 'aac',
            # Allow experimental features for ffmpeg
            '-strict', 'experimental',
        ],
    }

    # Download the YouTube video from the provided URL
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # List of URLs to download
        ydl.download(["https://youtu.be/iYaQ7NpoKFA"])
    # Notify the user when the download is finished
    print("Download completed!")

def hook_function(d):
    """
    Print a message when the video download is finished.
    Args:
        d (dict): Dictionary with progress data.
    """
    if d['status'] == 'finished':
        print(f'\nDone downloading video: {d["filename"]}')

if __name__ == "__main__":
    # Get the path for saving the video
    parentdir = setup_paths()
    # Download the YouTube video
    download_youtube_video(parentdir)
