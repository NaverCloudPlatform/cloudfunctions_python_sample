import calc
from sms_sender import SmsSender
from mail_sender import MailSender
from rss_news_parser import RssNewsParser
from datetime import datetime


def main(args):

    process_calc({"num1": 2, "num2": 3})
    #process_sens()
    #process_mail()


# cloud functions : calculator
def process_calc(args):

    num1 = args.get("num1", 1)
    num2 = args.get("num2", 2)

    result = calc.Calc.sum(num1, num2)

    print("## num1 : " + str(num1))
    print("## num2 : " + str(num2))
    print("## result : " + str(result))

    return {"payload": result}


# cloud functions : SENS
def process_sens():

    sms_info = {
        "type": "sms",
        "contentType": "comm",
        "countryCode": "82",
        "from": "01000000000",
        "to": [
            "01000000000"
        ],
        "content": "hello world"
    }

    res = SmsSender().req_sms(sms_info)

    print("response status:\n%d" % res.getcode())
    print("response info:\n%s" % res.info())
    print("response body:\n%s" % res.read())

    return {"result": "success"}


# cloud functions : Outbound mailer
def process_mail():

    current_date = datetime.today().strftime("%Y-%m-%d")
    mail_contents = RssNewsParser().news_rss_parser('NCP+네이버클라우드플랫폼')

    mail_info = {
        "senderAddress": "no_reply@company.com",
        "title": "네이버클라우드 플랫폼 뉴스 - ${current_date}",
        "body": mail_contents,
        "recipients": [
            {
                "address": "receiver@company.com",
                "name": "홍길동",
                "type": "R",
                "parameters": {
                    "current_date": current_date
                }
            }
        ],
        "individual": True,
        "advertising": False
    }

    res = MailSender().req_email_send(mail_info)

    print("response status:\n%d" % res.getcode())
    print("response info:\n%s" % res.info())
    print("response body:\n%s" % res.read())

    return {"result": "success"}


if __name__ == '__main__':
    main(None)