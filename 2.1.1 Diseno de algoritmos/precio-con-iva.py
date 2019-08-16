def main():
    price_without_iva = float(input("Price: "))

    iva = price_without_iva * 0.19

    print(f"Price of IVA = {iva}")
    print(f"Final price = {price_without_iva + iva}")


if __name__ == '__main__':
    main()
