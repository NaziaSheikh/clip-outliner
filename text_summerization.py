import streamlit as st
import requests
def app():
    def summarize(data):


        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data
        })
        return output



    st.title("Text summarizer")
    input_video = st.text_input("Enter the text/article etc.")
    if st.button("Summarize the text"):
        texte = summarize(input_video)
        st.write(texte)
