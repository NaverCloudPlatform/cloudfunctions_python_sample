import urllib.parse
import urllib.request
import ssl
import json
from base_auth_info import BaseAuthInfo


class SmsSender(BaseAuthInfo):

    auth_info = BaseAuthInfo()

    ep_path = auth_info.get_sens_ep_path()
    access_key = auth_info.get_access_key()
    sens_service_secrete = auth_info.get_sens_service_secrete()

    def req_sms(self, sms_info):
        context = ssl._create_unverified_context()

        req = urllib.request.Request(self.ep_path)

        req.add_header('X-NCP-auth-key', self.access_key)
        req.add_header('X-NCP-service-secret', self.sens_service_secrete)
        req.add_header('Content-Type', 'application/json')

        json_data = json.dumps(sms_info)
        json_data_bytes = json_data.encode('utf-8')

        response = urllib.request.urlopen(req, json_data_bytes, context=context)

        return response


if __name__ == '__main__':

    sms_info = {
        "type": "sms",
        "contentType": "comm",
        "countryCode": "82",
        "from": "",
        "to": [
            ""
        ],
        "content": "hello world"
    }

    SmsSender().req_sms(sms_info)
