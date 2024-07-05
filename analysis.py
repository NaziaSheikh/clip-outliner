import streamlit as st
import pandas as pd
from pytube import YouTube
import os
from st_clickable_images import clickable_images
import requests
@st.cache_data
def save_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    outfile=video.download()
    base,ext=os.path.splitext(outfile)
    filename=base+".mp3"
    counter = 1
    while os.path.exists(filename):
        # If the file exists, add a number suffix to the filename
        filename = f"{base}_{counter}.mp3"
        counter += 1
    os.rename(outfile,filename)
   
    return yt.title, filename, yt.thumbnail_url

def upload_to_AssemblyAI(video_location):
    CHUNK_SIZE = 5242880

    def read_file(filename):
        with open(filename, 'rb') as _file:
            while True:
                print("chunk uploaded")
                data=_file.read(CHUNK_SIZE)
                if not data:
                    break
                yield(data)
    upload_response=requests.post(upload_endpoints,headers=headers, data=read_file(video_location))
    print(upload_response.json())
    st.write(upload_response.json())

    audio_url=upload_response.json()['upload_url']
    print("uploaded to ",audio_url)
    return audio_url


st.title('YouTube Content Analyzer')
st.markdown("With this app you can audit a youtube channel to see if you'd like to sponsor them. All you have to do is pass a list of links to the videos of this channel and you will get a list of thumbnails, you can view:")
st.markdown("1. A summary of the video")
st.markdown("2. The topics that are discussed in the video")
st.markdown("3. Whether there are any sesitive topics discussed in the video.")
st.markdown("Make sure your links are in the format: https://www.youtube.com/watch?v=Mmt936kgot0 and not https://www.youtu.be/Mmt936kgot0")
default_bool=st.checkbox("Upload a default file")
if default_bool:
    file=open("D:\links.txt")
else:
    file=st.file_uploader("Upload the file that contains links to your video (.txt)")

if file is not None:
    dataframe=pd.read_csv(file,header=None)
    dataframe.columns=['urls']
    urls_list=dataframe['urls'].tolist()

    titles=[]
    locations=[]
    thumbnails=[]
    for video_urls in urls_list:
        yt_title, video_location, thumbnail_url=save_audio(video_urls)
        titles.append(yt_title)
        locations.append(video_location)
        thumbnails.append(thumbnail_url)

        selected_video = clickable_images(thumbnails,
                                          titles=titles,
                                          div_style={"height": "400px", "overflow-y": "auto"},
                                          img_style={"margin": "5px", "height": "150px"})
        st.markdown(f"Thumbnail #{selected_video} clicked" if selected_video>-1 else "No image clicked")
        if selected_video>-1:
            video_url=urls_list[selected_video]
            video_title=titles[selected_video]
            video_location=locations[selected_video]

            st.header(video_title)
            st.audio(video_location)




