import streamlit as st
import shutil

import os
import spotipy
import spotipy.oauth2 as oauth2
import yt_dlp
from youtube_search import YoutubeSearch
import multiprocessing
import urllib.request
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from pytube import Playlist
import platform

# Gestione della pagina corrente
if "page" not in st.session_state:
    st.session_state.page = "main_page"



def set_page_width():
    st.markdown(
        """
        <style>
            button[data-baseweb="tab"] {
                width: 100%
            }
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .block-container {
            max-width: 1200px;
            # padding-right: 50px;
            # padding-left: 50px;
            overflow-y: auto;  /* Permette lo scroll verticale se necessario */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.set_page_config(
    page_title="Compleanno Mara",
    page_icon="🎉️",  # Puoi usare un emoji o un percorso a un file .ico
)

def winner_page():
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            animation: fadeIn 2s ease-in-out, led 2.5s infinite;
        }

        .title {
            font-size: 60px;
        }

        .subtitle {
            font-size: 20px;
            padding-bottom: 40px;
            margin-top: -15px;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes led {
            0% { color: #fff; text-shadow: 0 0 5px #287233, 0 0 10px #287233, 0 0 20px #287233, 0 0 40px #287233; }
            50% { color: #fff; text-shadow: 0 0 10px #287233, 0 0 30px #287233, 0 0 30px #287233, 0 0 60px #287233; }
            100% { color: #fff; text-shadow: 0 0 5px #287233, 0 0 10px #287233, 0 0 20px #287233, 0 0 40px #287233; }
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    set_page_width()
    image_path = 'IMG_4576.png'  # Sostituisci con il percorso del tuo file

    # Mostra l'immagine
    _,c1,_ = st.columns([2,5,2])
    with c1:
        st.image(image_path, use_column_width=True)

    st.markdown('<h1 class="centered-title title">❤️️ Auguriiiiiiii! ❤️️</h1><h3 class="centered-title subtitle">- Hai vinto il tuo regalo -</h3>', unsafe_allow_html=True)
    st.balloons()

def main_page():    # if os.path.isfile('config.ini') or os.path.isfile('../config.ini'):
    #     import configparser
    #
    #     config = configparser.ConfigParser()
    #     config.read("config.ini")
    #     client_id = config["Settings"]["client_id"]
    #     client_secret = config["Settings"]["client_secret"]
    #     username = config["Settings"]["username"]
    # else:
    #     print("config.ini file not found...")
    #     client_id = input("Client ID: ")
    #     client_secret = input("Client secret: ")
    #     username = input("Spotify username: ")

    set_page_width()

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            animation: fadeIn 2s ease-in-out, led 2.5s infinite;
        }

        .title {
            font-size: 60px;
        }

        .subtitle {
            font-size: 20px;
            padding-bottom: 40px;
            margin-top: -15px;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes led {
            0% { color: #fff; text-shadow: 0 0 5px #287233, 0 0 10px #287233, 0 0 20px #287233, 0 0 40px #287233; }
            50% { color: #fff; text-shadow: 0 0 10px #287233, 0 0 30px #287233, 0 0 30px #287233, 0 0 60px #287233; }
            100% { color: #fff; text-shadow: 0 0 5px #287233, 0 0 10px #287233, 0 0 20px #287233, 0 0 40px #287233; }
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Inserire il titolo centrato
    st.markdown('<h1 class="centered-title title">🎉️ I regali vanno sudati 🎉️</h1><h3 class="centered-title subtitle">- Trova il codice segreto per sbloccare il regalo -</h3>', unsafe_allow_html=True)

    secret_code = st.text_input("Codice Super Segretissimo")

    # c1, c2 = st.columns(2)
    # with c1:
    yt_download_button = st.button("Sblocca Regalo", key='download_button_youtube', use_container_width=True)

    if yt_download_button and secret_code == '294':
        st.session_state.page = "new_page"
        st.rerun()
        st.balloons()
        st.info('Auguriiiiiiii 🎉🎉🎉🎉🎉🎉🎉🎉!')


    elif secret_code != '294' and yt_download_button:
        st.toast("⚠️ Ritenta sarai più fortunata")
        # Pulsante per simulare un errore
        st.snow()



if st.session_state.page == "main_page":
    main_page()
elif st.session_state.page == "new_page":
    winner_page()