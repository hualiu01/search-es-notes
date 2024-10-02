import requests
from requests.auth import HTTPBasicAuth 
import logging

logger = logging.getLogger(__name__)

def get_req(
        url: str, # do not put '/' in the end
        url_parameters: dict=None,  # to be binded to url
        auth_api_key:str=None,
        auth_un:str=None,
        auth_pw:str=None,
        http_headers:dict={'Accept': 'application/json'},
        timeout_seconds:float=5,
        allow_redirects:bool=True,
        ssl_verify:bool=True,
        ):
    
    session = requests.Session()

    # config auth
    if auth_api_key:
        session.headers.update({"Authorization": f"Bearer {auth_api_key}"})
    elif (auth_un and auth_pw): 
        session.auth = HTTPBasicAuth(auth_un, auth_pw)
    
    # config http headers
    session.headers.update(http_headers)

    # send request
    logger.info(f"sending GET http request to {url} with parameters {url_parameters}")
    response = session.get(
        url=url,
        params=url_parameters,
        timeout=timeout_seconds,
        allow_redirects=allow_redirects,
        verify=ssl_verify
        )

    # check response status
    if response.status_code != 200:
        response.raise_for_status()
    
    return response.json()
