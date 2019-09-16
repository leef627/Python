#由用户输入一元二次方程的三个系数，计算得出方程的根。考虑到无实数解，两个相同的解和两个不同的解等各种情况。
import math
while True:
    print('请按输入一元二次方程的三个系数')
    a = float(input('请输入a:\n'))
    b = float(input('请输入b:\n'))
    c = float(input('请输入c:\n'))
    if a==0:
        print('该方程不是一元二次方程!')
        continue
    if b * b - 4 * a * c < 0:
        print('该方程无解')
    if b * b - 4 * a * c == 0:
        print('该方程组有两个相同的解，即x1=x2=', -b / (2 * a))
    if b * b - 4 * a * c > 0:
        print('该方程组有两个不同的解，其中x1=', -(b + math.sqrt(b * b - 4 * a * c)) / (2 * a), 'x2=', -(b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
