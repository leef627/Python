import random

a = [random.randint(0, 100) for i in range(50)]
print(a)
i = len(a) - 1
while i >= 0:
    if a[i] % 2 == 1:
        del a[i]
    i -= 1
print(a)