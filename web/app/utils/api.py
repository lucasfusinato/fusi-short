import requests
import os
from http import HTTPStatus
from .errors import GenericError, ClientError

api_url = os.environ.get('API_URL')

def get_short_url(alias: str) -> dict:
    try:
        response = requests.get(
            url=f'{api_url}/short-url/{alias}',
            headers={
                'Accept': 'application/json',
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            response = error.response.json()
            raise ClientError(message=response['detail'], original_error=error)
        raise GenericError(original_error=error)
    except requests.exceptions.RequestException as error:
        raise GenericError(original_error=error)

def create_short_url(link: str, alias: str) -> dict:
    try:
        response = requests.post(
            url=f'{api_url}/short-url',
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            json={
                'link': link,
                'alias': alias
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == HTTPStatus.CONFLICT:
            response = error.response.json()
            raise ClientError(message=response['detail'], original_error=error)
        raise GenericError(original_error=error)
    except requests.exceptions.RequestException as error:
        raise GenericError(original_error=error)
        