import os
from bokeh.models.widgets import Div
import streamlit as st

def get_public_url(alias: str) -> str:
    public_url = os.environ.get('PUBLIC_URL')
    return f'{public_url}?open={alias}'

def get_open_alias_param() -> str:
    params = st.experimental_get_query_params()
    if 'open' in params:
        alias, = params['open']
        return alias
    return None

def redirect_to(link: str) -> None:
    if not link.startswith('http://') and not link.startswith('https://'):
        link = f'https://{link}'
    js = f"window.location.href = '{link}'"
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)