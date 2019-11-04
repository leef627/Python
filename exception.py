try:
    a=input('input a:')
    b=input('input b:')
    result=int(a)/int(b)
    print(result)
except ZeroDivisionError:
    print('0不能作为除数')
except ValueError:
    print('数值输入错误')
finally:
    print('I can catch errors')