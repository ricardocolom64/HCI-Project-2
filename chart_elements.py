import streamlit as st
import requests
import keys

def display_ratings(game_select):
    game_select.replace(" ", "-")
    game_select.lower()

    if game_select:
        ratings_url = "https://api.rawg.io/api/games?key={0}" \
                      "&{1}".format(keys.RAWG_API_KEY, game_select)
        ratings_dict = requests.get(ratings_url).json()
        st.write(ratings_dict)
def price_history():
    return -1

