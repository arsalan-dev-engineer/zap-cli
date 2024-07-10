import os
import sys
from pathlib import Path
import click
import yt_dlp

# --------------------
@click.group(help="A group of commands for downloading YouTube videos")
def yt_dl():
    """Main command group for YouTube video download."""
    pass

# --------------------

# Get the current directory of the script
currentdir = Path(__file__).resolve().parent
# Get the parent directory of the current directory
parentdir = currentdir.parent

# --------------------

@click.command("u", help="Input YouTube video URL.")
@click.argument("folder_name")
@click.argument("url")
def temp(folder_name, url):
    """Download a YouTube video given its URL into a specified folder."""
    # Define the base path where videos will be stored
    video_base_path = parentdir / "misc/youtube_videos"
    # Define the specific path for the video based on folder_name
    video_path = video_base_path / folder_name
    
    # Check if the specified directory does not exist
    if not video_path.exists():
        # Create the directory and any necessary parent directories
        video_path.mkdir(parents=True)
        click.echo(f"Directory '{folder_name}' does not exist. Creating directory.")

    # Define the options for yt_dlp to download video
    ydl_opts = {
        # Download the best video and best audio, then merge them into the best available format
        "format": "bestvideo+bestaudio/best",
        # Output template for the downloaded video files
        "outtmpl": str(video_path / "%(title)s.%(ext)s"),
        # Merge video and audio into MP4 format
        "merge_output_format": "mp4",
        # Download only a single video, not playlists
        "noplaylist": True,
        # Function to handle progress updates
        "progress_hooks": [hook_function],
        # Remove the cache directory after the download
        "rm_cache_dir": True,
        # Specify the location of the ffmpeg executable
        "ffmpeg_location": get_ffmpeg_path(),
        # Postprocessors to ensure correct video and audio formats
        "postprocessors": [{
            # Postprocess the video to convert it to the desired format
            'key': 'FFmpegVideoConvertor',
            # Set the output format to MP4
            'preferedformat': 'mp4',
        }],
        # Ensure that ffmpeg uses the correct codecs for audio and video
        "postprocessor_args": [
            # Use x264 for video encoding
            '-c:v', 'libx264',
            # Use AAC for audio encoding
            '-c:a', 'aac',
            # Ensure audio and video are in sync
            '-strict', 'experimental',
        ],
    }

    try:
        # Download the video using yt_dlp with specified options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        click.echo("Download complete.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")

# --------------------

@click.command("list", help="List available folders in youtube_videos.")
def list_folders():
    """List the folders inside youtube_videos."""
    # Define the base path where videos are stored
    video_base_path = parentdir / "misc/youtube_videos"
    # Check if the base path exists
    if not video_base_path.exists():
        click.echo("No folders available. The youtube_videos directory does not exist.")
        return

    # Get a list of folders inside the video_base_path
    folders = [f.name for f in video_base_path.iterdir() if f.is_dir()]
    # Check if there are any folders
    if folders:
        click.echo("Available folders:")
        # Print each folder name
        for folder in folders:
            click.echo(f"- {folder}")
    else:
        click.echo("No folders available.")

# --------------------

def hook_function(d):
    """
    Print a message when the video download is finished.
    Args:
        d (dict): Dictionary with progress data.
    """
    if d['status'] == 'finished':
        click.echo(f'\nDone downloading video: {d["filename"]}')

# --------------------

def get_ffmpeg_path():
    """Return the path to ffmpeg executable if available."""
    import shutil
    # Find the path to ffmpeg executable
    ffmpeg_path = shutil.which("ffmpeg")
    # Check if ffmpeg is found
    if ffmpeg_path:
        return ffmpeg_path
    else:
        click.echo("ffmpeg is not installed or not found in PATH.")
        sys.exit(1)

# --------------------

# Add the 'temp' command to the main command group
yt_dl.add_command(temp)
# Add the 'list_folders' command to the main command group
yt_dl.add_command(list_folders)

# Entry point of the script
if __name__ == "__main__":
    yt_dl()
