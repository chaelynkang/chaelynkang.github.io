# for i in range(0, 3, 1):
#    for j in range(0, 2, 1):
#        print("변수의 변화를 확인 : ", i, j)

for dan in range(2, 10):
    print("%d 단" % dan)
    for k in range(1, 10):
        print("%d X %d = %d" %(dan, k, dan*k))
