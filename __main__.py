import calc


def main(args):

    num1 = args.get("num1", 1)
    num2 = args.get("num2", 2)

    result = calc.Calc.sum(num1, num2)

    print("## num1 : " + str(num1))
    print("## num2 : " + str(num2))
    print("## result : "+str(result))

    return {"payload": result}


if __name__ == '__main__':
    main({"num1": 2, "num2": 3})