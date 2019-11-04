import math

while True:
    a = float(input('a\n'))
    b = float(input('b\n'))
    c = float(input('c\n'))
    if a + b < c or a + c < b or b + c < a:
        print('无法组成三角形')
        continue
    else:
        p = 1 / 2 * (a + b + c)
        z = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('三角形面积为', z)
        if a == b or a == c or b == c:
            print('三角为等腰三角形')
        if a == b == c:
            print('三角形为等边三角形')
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print('三角形为直角三角形')
        else:
            print('三角形为普通三角形')
