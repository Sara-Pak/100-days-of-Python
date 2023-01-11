# 1 ->need to import the pytube and os_sys library
# 2 ->allow input from user providing youtube link
# 3 ->create a filter that only extracts the audio from video link
# 4 ->create a path for the audio file, by using the os_sys module
# 5 ->convert the audio into a mp3 file format.

# 1 import
from pytube import YouTube
import os

# 2 input
yt = YouTube(str(input("Enter the YouTube link you want in MP3 format: \n>> ")))

# 3 extract audio
video = yt.streams.filter(only_audio=True).first()

# check for location to save file
print("Enter the location for file (leave blank for current location)")
location = str(input(">> ")) or '.'

# download the file
dl_file = video.download(path=location)

# save the file
base, ext = os.path.splitext(dl_file)
new_file = base + '.mp3'
os.rename(dl_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
