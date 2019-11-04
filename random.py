import random
L = [random.randint(1, 100) for x in range(10)]
A = [x for x in L if not x % 2]
print(L)
print("偶数列表：{0} 和为：{1}".format(A, sum(A)))