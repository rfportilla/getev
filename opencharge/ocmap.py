import logging
from collections import namedtuple
from pathlib import Path
import requests
import datetime
import json, yaml
from . import schemas
from .schemas import AbsOcmapAttr
from urllib.parse import urljoin

OCMAP_BASE_URL = 'https://api.openchargemap.io/v3/'

"""
What do I want to do??

* ?: I want to specify a route and get a list of charge stations with a given range.
* Easy: I want to find all charge stations within a range, given Lat, Long
* ?: I want to filter charge stations based on specific parameters (working, matches my car)

"""


def token_required(func):
    def wrapper(self, *args, **kwargs):
        self.bearer_client.bearer_token
        func(self, *args, **kwargs)

    return wrapper

class OcmapAuth(object):
    expiry_pct = 0.8  # Percentage used to calculate minimim time for refresh
    expiry_age = 1200  # Default to 20 mins
    auth_path = 'profile/authenticate'
    base_url = OCMAP_BASE_URL

    def __init__(self, api_key: str, email: str = None, password: str = None) -> None:
        """
        Initialize an instance of OcmapAuth class.
    
        This class is responsible for handling authentication with the Open Charge Map API.
        It takes three parameters: api_key, email, and password. The api_key is mandatory,
        while email and password are optional. If email and password are provided, they will
        be used for authentication. If only the api_key is provided, it will be used for
        unauthenticated requests.
    
        Parameters:
        api_key (str): The API key for authentication with the Open Charge Map API.
        email (str, optional): The email address for authentication. Defaults to None.
        password (str, optional): The password for authentication. Defaults to None.
    
        Returns:
        None: This method does not return any value. It initializes the OcmapAuth instance.
        """
        self.api_key = api_key
        self.email = email
        self.password = password
        self.is_valid(raise_error=True)
        self._bearer_token = None

    @property
    def bearer_token_expired(self):
        """
        Check if the current bearer token has expired.

        Parameters:
        self (OcmapClient): An instance of the OcmapClient class. This instance contains the necessary attributes for token expiration checking.

        Returns:
        bool: True if the bearer token has expired, False otherwise.
        """
        if (self._bearer_token_created is not None
            and datetime.datetime.now() < self._bearer_token_expiration):
            return False
        return True

    def _get_bearer_token(self, raise_error=True):
        h = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Accept': 'application/json',
        }
        b = {
            'emailaddress': self.email,
            'password': self.password,
        }

        r = requests.post(url=urljoin(self.base_url, self.auth_path), headers=h, json=b)
        if r.status_code == 200:
            self._bearer_token_created = datetime.datetime.now()
            rdata = r.json()['Data']
            self._bearer_token = rdata['access_token']
            return True
        elif raise_error:
            err_msg = 'Error authenticating; status code: {}, error message: {}'.format(
                r.status_code, r.content
            )
            raise requests.HTTPError(err_msg)
        return False

    @property
    def _bearer_token_expiration(self):
        return (self._bearer_token_created
                + datetime.timedelta(seconds=self.expiry_age * self.expiry_pct))

    @property
    def bearer_token(self):
        """
        Retrieves the bearer token for authentication with the Open Charge Map API.
        If the token is not available or has expired, it will be fetched using the provided credentials.

        Parameters:
        self (OcmapClient): An instance of the OcmapClient class. This instance contains the necessary attributes for token retrieval.

        Returns:
        str: The bearer token for authentication with the Open Charge Map API.
        """
        if self._bearer_token is None or self.bearer_token_expired:
            self._get_bearer_token()
        return self._bearer_token

    def is_valid(self, raise_error: bool = True):
        if self.api_key is not None:
            if (self.email is None or self.password is None):
                logging.warn('Email and password were not supplied.  Some endpoints require these for authentication.')
            return True
        elif raise_error:
            raise ValueError('An api_key is required for all endpoints.')
        logging.warn('An api_key was not provided.  This is required for all endpoints.')
        return False


class OcmapPoiClient(object):
    # https://openchargemap.org/site/develop/api#/operations/get-poi
    def retrievePoi(self, **kwargs):
        path = 'poi'
        schema = schemas.schema_pois
        filter_params = [
            'boundingbox',
            'camelcase',
            'chargepointid',
            'client',
            'compact',
            'connectiontypeid',
            'countrycode',
            'countryid',
            'dataproviderid',
            'distance',
            'distanceunit',
            'includecomments',
            'latitude',
            'levelid',
            'longitude',
            'maxresults',
            'opendata',
            'operatorid',
            'output',
            'polygon',
            'polyline',
            'statustypeid',
            'usagetypeid',
            'verbose',
        ]
        filter = {k: v for k, v in kwargs.items() if k in filter_params}
        h = {
            'X-API-Key': self.ocmapauth.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        r = requests.get(urljoin(OCMAP_BASE_URL, path), params=filter, headers=h)
        if r.status_code == 200:
            return AbsOcmapAttr.get_class(schema=schema, name='PoiResult')(r.json())
        else:
            err_msg = 'Error response; status code: {}, error message: {}'.format(
                r.status_code, r.content
            )
            raise requests.HTTPError(err_msg)


class OcmapCoreRefClient(object):
    # https://openchargemap.org/site/develop/api#/operations/get-referencedata
    def retrieveCoreRefData(self, **kwargs):
        path = 'referencedata'
        schema = schemas.schema_core_reference_data
        filter_params = [
            'countryid',
        ]
        filter = {k: v for k, v in kwargs.items() if k in filter_params}
        h = {
            'X-API-Key': self.ocmapauth.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        r = requests.get(urljoin(OCMAP_BASE_URL, path), params=filter, headers=h)
        if r.status_code == 200:
            return AbsOcmapAttr.get_class(schema=schema, name='CoreReferenceResult')(
                r.json()
            )

        err_msg = 'Error response; status code: {}, error message: {}'.format(
            r.status_code, r.content
        )
        raise requests.HTTPError(err_msg)


class OcmapCommentCheckinClient(object):
    def postComment(self, chargePointID, **kwargs):
        path = 'comment'
        schema = schemas.schema_comment_checkin_response
        params = [
            'commentTypeID',
            'userName',
            'comment',
            'rating',
            'relatedURL',
            'checkinStatusTypeID',
        ]
        data = {k: v for k, v in kwargs.items() if k in params}
        data['chargePointID'] = chargePointID
        h = {
            'X-API-Key': self.ocmapauth.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.bearer_token,
        }
        r = requests.post(urljoin(OCMAP_BASE_URL, path), json=data, headers=h)
        if r.status_code == 200:
            return AbsOcmapAttr.get_class(schema=schema, name='CommentCheckinResult')(
                r.json()
            )
        err_msg = 'Error response; status code: {}, error message: {}'.format(
            r.status_code, r.content
        )
        raise requests.HTTPError(err_msg)


class OcmapAddMediaClient(object):
    def addMedia(self, chargePointID, **kwargs):
        path = 'profile/authenticate'
        schema = schemas.schema_authentication_result


# Open API spec
from openapi_core import OpenAPI 
class OcmapOpenApiDefClient(object):
    path = 'openapi'
    #schema = schemas.schema_open_api_result

    def retrieveOpenApiDef(self, **kwargs):
        path = 'openapi'
        # schema = schemas.schema_open_api_result
        filter_params = []
        filter = {k: v for k, v in kwargs.items() if k in filter_params}
        h = {
            'X-API-Key': self.ocmapauth.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        r = requests.get(urljoin(OCMAP_BASE_URL, path), params=filter, headers=h)
        if r.status_code == 200:
            return r.text
        else:
            err_msg = 'Error response; status code: {}, error message: {}'.format(
                r.status_code, r.content
            )
            raise requests.HTTPError(err_msg)


class OcmapClient(
    OcmapPoiClient,
    OcmapCoreRefClient,
    OcmapCommentCheckinClient,
    OcmapAddMediaClient,
    OcmapOpenApiDefClient,
):
    ocmapauth = None

    def __init__(self, ocmap_auth: OcmapAuth):
        self.ocmapauth = ocmap_auth
        #self._bearer_token = None
        #self._bearer_token_expiration = datetime.datetime.now() - datetime.timedelta(seconds=60)
        #self._bearer_token_created = None
        #self._bearer_token_expiry = None

    @property
    def bearer_token(self):
        return self.ocmapauth.bearer_token
 

if __name__ == '__main__':
    o = OcmapAuth('abc123')
