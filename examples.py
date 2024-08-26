# This gives some sample code for the OCMap class.

# Fill in required connection parameters.  These must be set up at OCMap site.
api_key = '01234567-89ab-cdef-0123-456789abcdef'
email = '<yourname@example.com>'
passwd = '<abc123>'



# Retrieve POIs: this retrieves 100 POIs.  Filters may be passed in.  Overall, this is the basic format for all Ocmap operations. 
from opencharge.ocmap import OcmapClient, OcmapAuth

ocmap_auth = OcmapAuth(api_key=api_key, email=email, password=passwd)
clt = OcmapClient(ocmap_auth)
pois = clt.retrievePoi()
print(pois[0])

# Authenticate: this is not required as it will be called implicitly when necessary, but you can test credentials with this.
bt = clt.bearer_token

# Filters: may be passed into some of the methods to limit the results.  
pois = clt.retrievePoi(maxresults=5, latitude=35.75989070730711, longitude=-78.63918883082202, distance=3, distanceunit='miles')

