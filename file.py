with open('1.txt', 'r') as f:
    digital = 0
    lowercase = 0
    uppercase = 0
    other = 0
    while True:
        c = f.read(1)
        if not c:
            break
        elif str.isdigit(c):
            digital += 1
        elif str.isupper(c):
            uppercase += 1
        elif str.islower(c):
            lowercase += 1
        else:
            other += 1
print('大写字母有', uppercase, '个')
print('小写字母', lowercase, '个')
print('数字字符', digital, '个')
print('其他字符', other, '个')
