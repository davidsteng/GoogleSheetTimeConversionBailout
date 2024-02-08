f1 = open("MinSecFormat.txt", 'r')
f2 = open("HourMinSec.txt", 'w')
temp = f1.readlines()
print(temp)
temp2 = []
for i in range(len(temp)):
    temp2.append("00:" + temp[i])
    f2.write("00:" + temp[i])
print(temp2)
#f2.write(temp)
f2.close()