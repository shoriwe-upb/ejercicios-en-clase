from math import sin, pi


# a is the known angle and c is the lower leg of the triangle
def calculate_height(a, c):
    third_angle = (90 - a) * pi / 180
    a = a * pi / 180
    height = sin(a) / (sin(third_angle) / c)

    return height


def main():
    a = float(input("Angle: "))
    c = float(input("Leg: "))

    result = calculate_height(a, c)

    print(f"{result}m")


if __name__ == '__main__':
    main()
