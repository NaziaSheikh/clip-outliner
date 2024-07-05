import streamlit as st
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
def app():
    st.title("Meaning, Antonym, Synonym")
    word = st.text_input("Enter a word:")
    if word:
        synsets = wordnet.synsets(word)
        if synsets:
            st.subheader("Meaning:")
            st.write(synsets[0].definition())
            st.subheader("Synonyms:")
            synonyms = set()
            for syn in synsets:
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())
            st.write(", ".join(synonyms))

            st.subheader("Antonyms:")
            antonyms = set()
            for syn in synsets:
                for lemma in syn.lemmas():
                    if lemma.antonyms():
                        antonyms.add(lemma.antonyms()[0].name())
            if antonyms:
                st.write(", ".join(antonyms))
            else:
                st.write("No antonyms found.")
