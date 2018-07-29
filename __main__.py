import calc
import json
from sms_sender import SmsSender

# cloud function : calculator

# def main(args):
#
#     num1 = args.get("num1", 1)
#     num2 = args.get("num2", 2)
#
#     result = calc.Calc.sum(num1, num2)
#
#     print("## num1 : " + str(num1))
#     print("## num2 : " + str(num2))
#     print("## result : "+str(result))
#
#     return {"payload": result}


# cloud function : SENS

def main(args):

    res = SmsSender.req_sms()

    print("response status:\n%d" % res.getcode())
    print("response info:\n%s" % res.info())
    print("response body:\n%s" % res.read())

    return {"result": "success"}


if __name__ == '__main__':
    # main({"num1": 2, "num2": 3})
    main(None)