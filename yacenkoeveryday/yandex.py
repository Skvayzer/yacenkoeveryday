import requests
import pprint
import urllib.parse

targetUrl = "paste_image_url_here in yandex disk"
url = "https://cloud-api.yandex.net/v1/disk/public/resources?public_key=" + urllib.parse.quote( targetUrl, safe = "" )

responseData = requests.get( url )
if responseData.headers[ "content-type" ] in [ "application/json; charset=utf-8", "application/json" ]:
    print( pprint.pformat( responseData.json() ) )
else:
    print( responseData )