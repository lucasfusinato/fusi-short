import streamlit as st
from ..utils.api import get_short_url
from ..utils.url import redirect_to
from ..utils.errors import CustomError

def render(alias: str) -> None:
    try:
        short_url = get_short_url(alias=alias)
        link = short_url['link']
        st.markdown(f'You\'ll be redirect to {link}, wait a second...')
        redirect_to(link=link)
    except CustomError as error:
        st.error(error.get_message())