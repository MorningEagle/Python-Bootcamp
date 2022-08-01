from moviepy.editor import VideoFileClip
from urllib.request import urlopen


urls = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'

def load_vid(url: str) -> bytes:
        """Load video file from url path

        Args:
            url (str): url path of your file

        Returns:
            bytes: bytes of this file
        """
        with urlopen(url) as vid:
               return vid.read()
               
               
def conv_мid(url_vid: str):
        """Converter from video to GIF
        """
        with open('video.mp4', 'wb+') as vid:
          vid.write(load_vid(url_vid))
          
        videoClip = VideoFileClip('video.mp4')
        videoClip.write_gif('TikTok-example-1.gif')
        
conv_мid(urls)      
        