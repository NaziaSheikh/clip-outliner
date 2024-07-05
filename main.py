import streamlit as st
from streamlit_option_menu import option_menu



import video_summerization, text_summerization,pro,meaning,audio,about

st.set_page_config(
    page_title="Clip Outliner",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Clip Outliner ',
                options=['Video Summarization','About','Text Summarization','Info Summarization','Word Meaning','Translator/Audio'],
                icons=['house-fill','person-circle','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',

                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "Video Summarization":
            video_summerization.app()
        if app == "Text Summarization":
            text_summerization.app()
        if app == "Info Summarization":
            pro.app()
        if app == "Word Meaning":
            meaning.app()
        if app == "Translator/Audio":
            audio.app()
        if app == "About":
            about.app()




    run()
