import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
from os.path import join
import requests

def app():

        def transciption(addons):
            vid_id = addons
            data = yta.get_transcript(vid_id)
            transcript = []
            for value in data:
                for key, val in value.items():
                    if key == 'text':
                        transcript.append(val)
            final_tra = "\n".join(transcript)
            return final_tra

        def summarize(data):
            API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
            headers = {"Authorization": "Bearer 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"}
            datal = data
            minL=142


            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": data,
                "parameters":{"min_length":minL}

            })

            return output
        st.title("Video summarizer")
        input_video = st.text_input("Enter the video link")
        if st.button("Transcript the following video"):
            trans = transciption(input_video)
            st.write(trans)
        if st.button("Provide summary of the video"):
            st.header("Summary of the video")
            transp=transciption(input_video)
            summary = summarize(transp)
            st.write(summary)




