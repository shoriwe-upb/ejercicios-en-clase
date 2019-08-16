def count(to_pay, recieved):
    money_return = recieved - to_pay
    result = {}
    for buck in (100000, 50000, 20000, 10000, 5000, 2000, 1000):
        if money_return / buck >= 1:
            number_of_bucks = money_return // buck
            money_return -= buck * number_of_bucks
            result[buck] = number_of_bucks

    return result


def main():
    price = int(input("Price: "))
    recieved = int(input("Money recieved: "))
    result = count(price, recieved)
    for buck in result.keys():
        print(buck, "--->", result[buck])

if __name__ == '__main__':
    main()