import hashlib
import hmac
import base64
import time
import urllib.parse
import urllib.request
import ssl
import json
from base_auth_info import BaseAuthInfo


class MailSender(BaseAuthInfo):

    auth_info = BaseAuthInfo()

    ep_path = auth_info.get_mail_ep_path()
    api_key = auth_info.get_api_key()
    access_key = auth_info.get_access_key()
    access_secrete = auth_info.get_access_secrete()

    def req_email_send(self, mail_info):
        context = ssl._create_unverified_context()

        req = urllib.request.Request(self.ep_path)

        timestamp = self.get_timestamp()

        req.add_header('x-ncp-apigw-timestamp', timestamp)
        req.add_header('x-ncp-iam-access-key', self.access_key)
        req.add_header('x-ncp-apigw-signature-v1', self.make_signature(timestamp))
        req.add_header('Content-Type', 'application/json')

        json_data = json.dumps(mail_info)
        json_data_bytes = json_data.encode('utf-8')

        response = urllib.request.urlopen(req, json_data_bytes, context=context)

        return response

    @staticmethod
    def get_timestamp():
        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
        return timestamp

    def make_signature(self, timestamp):

        access_secrete_bytes = bytes(self.access_secrete, 'UTF-8')

        method = "POST"
        uri = "/api/v1/mails"

        message = method + " " + uri + "\n" + timestamp + "\n" + self.access_key
        message = bytes(message, 'UTF-8')
        signing_key = base64.b64encode(hmac.new(access_secrete_bytes, message, digestmod=hashlib.sha256).digest())

        return signing_key


if __name__ == '__main__':

    mail_info = {
        "senderAddress": "no_reply@company.com",
        "title": "${customer_name}님 반갑습니다. ",
        "body": "귀하의 등급이 ${BEFORE_GRADE}에서 ${AFTER_GRADE}로 변경되었습니다.",
        "recipients": [
            {
                "address": "changhyeon.heo@navercorp.com",
                "name": "홍길동",
                "type": "R",
                "parameters": {
                    "customer_name": "홍길동",
                    "BEFORE_GRADE": "SILVER",
                    "AFTER_GRADE": "GOLD"
                }
            }
        ],
        "individual": True,
        "advertising": False
    }

    MailSender().req_email_send(mail_info)