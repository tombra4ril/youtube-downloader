import pytube
import requests

def main():
  url = ""
  while not url:
    print(f"Enter q to stop!!")
    url = str(input("Please enter the url to the youtube site: "))
  response = requests.get(url)
  print(f"Status code: {response.status_code}")
  if response.status_code == 200:
    print(f"Connected successfully!")
    check_site = True
    print(f"Do you want a video or a playlist download? ")
    download = input("p - playlist    v - video(Default)")
    if download == "p" or download == "P":
      connect_youtube_playlist(url)
    elif download == "v" or download == "V" or download == "":
      connect_youtube(url)

def connect_youtube(url):
  stream_itags = {"360p": "18", "480p": "135", "720p": "22"}
  video = pytube.YouTube(url) 
  # get the video
  codec = None
  while codec not in stream_itags:
    print(f"360p downloads 360 pixels - Press Enter for Default(720p)")
    codec = str(input("Enter the type of codec for download: "))
    if codec == "":
      codec = stream_itags["720p"]
  stream = video.streams.get_by_itag(stream_itags[codec])
  print(f"Downloading...")
  stream.download()
  print(f"Completed donwload")

def connect_youtube_playlist(url):
  stream_itags = {"360p": "18", "480p": "135", "720p": "22"}
  playlist = pytube.Playlist(url) 
  # get the video
  codec = None
  while codec not in stream_itags:
    print(f"360p downloads 360 pixels - Press Enter for Default(720p)")
    codec = str(input("Enter the type of codec for download: "))
    if codec == "":
      codec = stream_itags["720p"]

  #download playlists
  start_count = 1
  print(f"Number of videos in playlist is {len(playlist)}")
  while start_count >= len(playlist):
    print(f"Press Enter to start from the begining!")
    start_count = int(input("What position of the playlist do you want to start from? "))

  start_count -= 1
  for _, url in enumerate(playlist):
    if _ < start_count:
      continue
    video = pytube.YouTube(url)    
    stream = video.streams.get_by_itag(stream_itags[codec])
    print(f"Downloading video {_ + 1}...")
    stream.download()
    print(f"Completed donwload of video {_ + 1}")

if __name__ == "__main__":
  main()
  