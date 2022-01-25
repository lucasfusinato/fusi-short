import streamlit as st
st.set_page_config()

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)

from .utils.url import get_open_alias_param
from .pages import short_url, redirect_url

def render():
    open_alias = get_open_alias_param()
    if open_alias is None:
        short_url.render()
    else:
        redirect_url.render(alias=open_alias)

if __name__ == '__main__':
    render()