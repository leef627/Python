import math
from xml.etree.ElementTree import PI

while True:
    print('输入圆的半径')
    r = float(input('r\n'))
    if r < 0:
        print('不成立，重新输入')
        continue
    else:
        z = (r ** 2) * 3.14
    print(z)
