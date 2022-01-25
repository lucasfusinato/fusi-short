from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from http import HTTPStatus
from ..utils import database

router = APIRouter()

class PostShortUrlIn(BaseModel):
    link: str
    alias: Optional[str] = None

class PostShortUrlOut(BaseModel):
    alias: str

class GetShortUrlOut(BaseModel):
    link: str

@router.post('/short-url', response_model=PostShortUrlOut)
def post_short_url(short_url: PostShortUrlIn):
    link = short_url.link
    alias = short_url.alias
    if alias is None or len(alias) == 0:
        alias = str(uuid4())
    elif database.is_short_url_exists(alias=alias):
        return HTTPException(status_code=HTTPStatus.CONFLICT, detail='Alias already used. Could you choose another one, please?')
    database.set_short_url(alias=alias, link=link)
    return PostShortUrlOut(alias=alias)

@router.get('/short-url/{alias}', response_model=GetShortUrlOut)
def get_short_url(alias: str):
    link = database.get_short_url_link(alias)
    if link is None:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail='Sorry, but alias doesn\'t match any registerd short url.')
    return GetShortUrlOut(link=link)