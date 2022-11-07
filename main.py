from pytube import YouTube

link = input("Enter url: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("enter the option to download format")
dn_option = int(input("Enter the option: "))
dn_video = videos[dn_option]
dn_video.download()

print("Download successfully")