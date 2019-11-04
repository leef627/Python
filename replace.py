fp1 = open("1.txt", "r")
fp2 = open("2.txt", "w")

for s in fp1.readlines():
    fp2.write(s.replace('Hello','Hi'))

fp1.close()
fp2.close()
