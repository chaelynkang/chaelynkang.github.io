list1 = []
list2 = []
value = 1


for i in range(0, 3):
    for j in range(0, 4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []
print(list2)

for i in range(0, 3):
    for j in range(0, 4):
        print("%3d" % list2[i][j], end = " ")
    print("")
    