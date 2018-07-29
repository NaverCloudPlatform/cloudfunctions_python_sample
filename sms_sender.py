import urllib.parse
import urllib.request
import ssl
import json

API_HOST = 'https://api-sens.ncloud.com'


# NCP Access Key ID
AUTH_KEY = 'qEvQEqjALeNxsOXqAa0F'
# SENS project secret key
SERVICE_SECRET = '3d1fff9635ce4faa8f3912168c7ab0c1'
# SENS project name
PROJECT_NAME = 'first_project'
# SENS service id
SERVICE_ID = 'ncp:sms:kr:253463621387:first_project'
# Request URL
FULL_PATH = API_HOST + '/v1/sms/services/' + SERVICE_ID + '/messages'
# Request Body
data = {
  "type": "sms",
  "contentType": "comm",
  "countryCode": "82",
  "from": "01071097007",
  "to": [
    "01071097007"
  ],
  "content": "hello world"
}


class SmsSender:

    @staticmethod
    def req_sms():
        context = ssl._create_unverified_context()

        req = urllib.request.Request(FULL_PATH)

        req.add_header('X-NCP-auth-key', 'qEvQEqjALeNxsOXqAa0F')
        req.add_header('X-NCP-service-secret', '3d1fff9635ce4faa8f3912168c7ab0c1')
        req.add_header('Content-Type', 'application/json')

        json_data = json.dumps(data)
        json_data_bytes = json_data.encode('utf-8')

        response = urllib.request.urlopen(req, json_data_bytes, context=context)

        return response