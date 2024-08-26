from copy import deepcopy
import datetime
import unittest
from unittest.mock import MagicMock
import requests_mock
import requests
from urllib.parse import urljoin

import context, data, json, uuid, yaml

from opencharge import schemas
from opencharge.ocmap import OcmapClient, OcmapAuth, OCMAP_BASE_URL
from opencharge.schemas import AbsOcmapAttr


USE_REAL_HTTP = False
API_KEY = '01234567-89ab-cdef-0123-456789abcdef'

class GetTest(object):
    def test_get_class(self):
        # Generic test to verify that the generic Ocmap properties can be retrieved
        klass = AbsOcmapAttr.get_class(self.schema)

        self.assertIsNotNone(klass)
        for attr in ['schema', 'raw_data']:
            self.assertTrue(hasattr(klass, attr))


    def test_klass_init(self):
        # Generic test to verify that Ocmap Attr object has expected attributes 
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f'Failed to get class: {e}')
        if isinstance(self.schema, (list, tuple)):
            for attr in self.schema[0]().schema.keys():
                self.assertTrue(hasattr(obj[0], attr))
        else:
            for attr in self.schema.keys():
                self.assertTrue(hasattr(obj, attr))

    @requests_mock.Mocker()
    def test_get_data(self, mock_request):
        '''
            Test successful GET request to an Ocmap API endpoint.
            This test uses a mocking library to intercept and validate the request.
        '''
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        for t in self.tcases:
            mock_request.get(self.path, text=t['response'], real_http=USE_REAL_HTTP)
            ocmap_attr = getattr(clt, self.func_call)()

            if isinstance(self.schema, (list, tuple)):
                ocmap_attr = ocmap_attr[0]

            r = t['expected']
            o = ocmap_attr
            for i in range(len(r)-1):
                self.assertTrue(hasattr(o, r[i]), 'Missing attribute: "{}" not in response\n{}'.format(r[i], ocmap_attr))
                o = getattr(o, r[i])

            self.assertEqual(r[-1], o)

    @requests_mock.Mocker()
    def test_dir_attrs(self, mock_request):
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        mock_request.get(self.path, text=json.dumps(self.init_data), real_http=USE_REAL_HTTP)

        ocmap_attr = getattr(clt, self.func_call)()
        if isinstance(self.schema, (list, tuple)):
            ocmap_attr = ocmap_attr[0]

        props = dir(ocmap_attr)
        for attr in (ocmap_attr.schema):
            self.assertIn(attr, props)

class TestRetrievePoiList(unittest.TestCase, GetTest):
    schema = schemas.schema_pois
    path = urljoin(OCMAP_BASE_URL, 'poi')
    func_call = 'retrievePoi'
    init_data = json.loads(data.TEST_POI_RESPONSE)

    tcases = [
        {'send': {}, 'response': data.TEST_POI_RESPONSE, 'headers': {'X-API-Key': API_KEY},
            'expected': ['DataProvider', 'WebsiteURL', 'http://www.afdc.energy.gov/']},
        {'send': {}, 'response': data.TEST_POI_RESPONSE, 'headers': {'X-API-Key': API_KEY},
            'expected': ['StatusType', 'IsOperational', True]},
    ]

    def test_klass_properties_init(self):
        test_matrix = {
            'IsRecentlyVerified': True,
            'ID': 221862,
            'UUID': uuid.UUID('080FA53F-42A4-42C2-9F9C-1C9B08CD2759'),
            'DataProviderID': 2,
            'UsageTypeID': 2,
            'SubmissionStatusTypeID': 100,
            'DateLastStatusUpdate': datetime.datetime.fromisoformat('2024-02-20T09:55:00Z'),
        }
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f'Failed to create instance: {e}')
        self.assertGreater(len(obj), 0)
        poi = obj[0]
        for attr, expected in test_matrix.items():
            self.assertEqual(getattr(poi, attr), expected, 'Unexpected value for attribute: {}'.format(attr))
        
    def test_subklass_properties(self):
        test_matrix = {
            'DataProvider': 'DataProvider',
            'UsageType': 'UsageType',
            'StatusType': 'StatusType',
            'AddressInfo': 'AddressInfo',
            'Connections': 'list',
        }
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f"Failed to create instance: {e}")
        self.assertGreater(len(obj), 0)
        poi = obj[0]
        for attr, expected in test_matrix.items():
            self.assertRegex(str(type(getattr(poi, attr))), expected)

    def test_connections_attr(self):
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f"Failed to create instance: {e}")
        self.assertGreater(len(obj), 0)
        poi = obj[0]
        conns = poi.Connections
        self.assertGreater(len(conns), 0)
        for conn in conns:
            self.assertRegex(str(type(conn)), 'ConnectionInfo')

class TestCoreReferenceList(unittest.TestCase, GetTest):
    schema = schemas.schema_core_reference_data
    path = urljoin(OCMAP_BASE_URL, 'referencedata')
    func_call = 'retrieveCoreRefData'
    init_data = json.loads(data.TEST_CORE_REFERENCE_RESPONSE)
    tcases = [
        {'send': {}, 'response': data.TEST_CORE_REFERENCE_RESPONSE, 'headers': {'X-API-Key': API_KEY},
            'expected': ['ChargerTypes', [AbsOcmapAttr.get_class(schemas.schema_level_type, 'LevelType')(x) for x in [
                            {
                                'Comments': 'Under 2 kW, usually domestic socket types',
                                'IsFastChargeCapable': False,
                                'ID': 1,
                                'Title': 'Level 1 : Low (Under 2kW)'
                            },
                            {
                                'Comments': 'Over 2 kW, usually non-domestic socket type',
                                'IsFastChargeCapable': False,
                                'ID': 2,
                                'Title': 'Level 2 : Medium (Over 2kW)'
                            },
                            {
                                'Comments': '40KW and Higher',
                                'IsFastChargeCapable': True,
                                'ID': 3,
                                'Title': 'Level 3:  High (Over 40kW)'
                            }
                        ]]]
        },
    ]

    def test_klass_properties_init(self):
        attrs = ['ChargerTypes', 'ConnectionTypes', 'CurrentTypes', 'Countries', 'Operators', 'StatusTypes',
                 'SubmissionStatusTypes', 'UsageTypes', 'UserCommentTypes', 'CheckinStatusTypes', 'DataTypes',
                 'MetadataGroups']
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f'Failed to create instance: {e}')
        for attr in attrs:
            self.assertTrue(hasattr(obj, attr))

    def test_connection_types(self):
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f'Failed to create instance: {e}')
        connection_types = obj.ConnectionTypes
        for ctype in connection_types:
            self.assertRegex(str(type(ctype)), 'ConnectionType')

    def test_checkin_status_types(self):
        try:
            obj = AbsOcmapAttr.get_class(self.schema)(self.init_data)
        except Exception as e:
            self.fail(f'Failed to create instance: {e}')
        
        checkin_status_types = obj.CheckinStatusTypes
        for ctype in checkin_status_types:
            self.assertRegex(str(type(ctype)), 'CheckinStatusType')

class TestRetrieveOpenApiDef(unittest.TestCase):
    schema = schemas.schema_open_api_result
    path = urljoin(OCMAP_BASE_URL, 'openapi')
    func_call = 'retrieveOpenApiDef'
    init_data = yaml.safe_load(data.TEST_OPENAPI_RESPONSE)
    cls_name = 'OpenApiResult'
    obj_attrs = ['openapi', 'info']
    tcases = [
        {'send': {}, 'response': data.TEST_OPENAPI_RESPONSE,
         'expected': ['info', 'title', 'Open Charge Map API']},
        {'send': {}, 'response': data.TEST_OPENAPI_RESPONSE,
         'expected': ['info', 'servers', 'url', r'https://api.openchargemap.io/v3']},
    ]

    def test_klass_properties_init(self):
        try:
            obj = AbsOcmapAttr.get_class(self.schema, self.cls_name)(yaml.safe_load(self.tcases[0]['response']))
        except Exception as e:
            self.fail(f'Failed to create instance: {e}')
        for attr in self.obj_attrs:
            self.assertTrue(hasattr(obj, attr))

    @requests_mock.Mocker()
    def test_get_data(self, mock_request):
        '''
            OpenAPI response is a bit different from other OCMap responses in that 
               it is a reference to the API rather than part of the service.  As such,
               we expect the response to be a simple dictionary.
            "tcases" is a list of test cases with expected values in the response.
            The "expected" key points to a list of paths and a final value.  
                i.e. [[..., 'path', 'to', 'key', <expected value>], ...]
        '''
        tcases = [
            {'send': {}, 'response': data.TEST_OPENAPI_RESPONSE,
             'expected': [['info', 'title', 'Open Charge Map API'],
                      ['paths', '/poi', 'get', 'operationId', 'get-poi']
            ]},
        ]
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        for t in tcases:
            mock_request.get(self.path, text=t['response'], real_http=USE_REAL_HTTP)
                
            oa_spec = yaml.safe_load(getattr(clt, self.func_call)())
            for r in t['expected']:
                o = oa_spec
                for i in range(len(r)-1):
                    self.assertIn(r[i], o, 'Missing attribute: "{}" not in response\n{}'.format(r[i], oa_spec))
                    o = o.get(r[i])
                self.assertEqual(o, r[-1])


class TestAuthenticateUser(unittest.TestCase):

    @requests_mock.Mocker()
    def test_get_bearer_token(self, mock_request):
        '''
            Test successful authentication and retrieval of a Bearer token.
            This test uses a mocking library to intercept and validate the request.
        '''
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=data.TEST_AUTH_RESPONSE)
        bearer_token = clt.bearer_token
        self.assertRegex(bearer_token, 'Supercalifragilisticexpialidocious')

    @requests_mock.Mocker()
    def test_bearer_expired_called(self, mock_request):
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=data.TEST_AUTH_RESPONSE)

        with unittest.mock.patch('__main__.OcmapAuth.bearer_token_expired', new_callable=unittest.mock.PropertyMock) as mock_exp:
            mock_exp.return_value = False
            clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
            clt.ocmapauth._get_bearer_token()
            clt.bearer_token
        mock_exp.assert_called_once_with()

    @requests_mock.Mocker()
    def test_bearer_expiration(self, mock_request):
        resp_data = deepcopy(data.TEST_AUTH_RESPONSE)
        resp_data['DateCreated'] = datetime.datetime.now().isoformat()
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=resp_data)

        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        clt.ocmapauth._get_bearer_token()
        # set bearer token expiration datetime to expired
        clt.ocmapauth._bearer_token_created = datetime.datetime.now() - datetime.timedelta(seconds=clt.ocmapauth.expiry_age)
        with unittest.mock.patch.object(OcmapAuth, '_get_bearer_token', return_value=True) as mock_get_bearer:
            clt.bearer_token
        mock_get_bearer.assert_called_once_with()

    @requests_mock.Mocker()
    def test_bearer_not_expired(self, mock_request):
        resp_data = deepcopy(data.TEST_AUTH_RESPONSE)
        resp_data['DateCreated'] = datetime.datetime.now().isoformat()
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=resp_data)
        
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        clt.ocmapauth._get_bearer_token()

        with unittest.mock.patch.object(OcmapAuth, '_get_bearer_token', return_value=True) as mock_get_bearer:
            clt.bearer_token
        mock_get_bearer.assert_not_called()

class TestCommentCheckinClient(unittest.TestCase):
    func_call = 'postComment'

    @requests_mock.Mocker()
    def test_submit_comment(self, mock_request):
        resp_data = data.TEST_COMMENT_CHECKIN_RESPONSE
        url_path = 'https://api.openchargemap.io/v3/comment'
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=data.TEST_AUTH_RESPONSE)
        mock_request.post(url_path, status_code=200, json=resp_data)
        headers = {'Authorization': 'Bearer {}'.format(data.TEST_AUTH_RESPONSE['Data']['access_token'])}
        comment_data = {
            'commentTypeID': 10,
            'userName': 'testuser',
            'comment': 'This is a test comment.',
            'rating': 4,
            'relatedURL': 'https://test.com/ratingSample',
            'checkinStatusTypeID': 30,
        }

        #resp = requests.post(url_path, data=body, headers=headers)
        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        r = getattr(clt, self.func_call)(61827, **comment_data)
        print(r.status)
        for attr in ('status', 'description'):
            self.assertEqual(getattr(r, attr), resp_data[attr])

    @requests_mock.Mocker()
    def test_dir_attrs(self, mock_request):
        resp_data = data.TEST_COMMENT_CHECKIN_RESPONSE
        url_path = 'https://api.openchargemap.io/v3/comment'
        mock_request.post('https://api.openchargemap.io/v3/profile/authenticate', status_code=200, json=data.TEST_AUTH_RESPONSE)
        mock_request.post(url_path, status_code=200, json=resp_data)
        headers = {'Authorization': 'Bearer {}'.format(data.TEST_AUTH_RESPONSE['Data']['access_token'])}

        clt = OcmapClient(OcmapAuth('abc123', 'notreal@test.com', 'password1'))
        r = getattr(clt, self.func_call)(61827)
        props = dir(r)
        for attr in (r.schema):
            self.assertIn(attr, props)


if __name__ == '__main__':
    unittest.main(module='__main__')#, defaultTest='TestRetrieveOpenApiDef.test_dir_attrs')

