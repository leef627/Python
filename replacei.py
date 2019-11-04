import re

a = "i am a teacher,i am man, and i am 38 years old.I am not a businessman."
pattern = re.compile(r'(?:[^\w]|\b)i(?:[^\w])')
while True:
    result = pattern.search(a)
    if result:
        if result.start(0) != 0:
            a = a[:result.start(0) + 1] + 'I' + a[result.end(0) - 1:]
        else:
            a = a[:result.start(0)] + 'I' + a[result.end(0) - 1:]
    else:
        break
print(a)
