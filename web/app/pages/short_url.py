import streamlit as st
from ..utils.url import get_public_url
from ..utils.api import create_short_url
from ..utils.errors import CustomError
    
def render() -> None:
    with st.form('short_url_form'):
        link = st.text_input('URL to short: ')
        alias = st.text_input('Custom alias: ')

        submitted = st.form_submit_button('Short URL')
        if submitted:
            try:
                short_url = create_short_url(link=link, alias=alias)
                public_url = get_public_url(alias=short_url['alias'])
                st.write(f'URL was shorted with success! Access your site with following link: {public_url}')
            except CustomError as error:
                st.error(error.get_message())
