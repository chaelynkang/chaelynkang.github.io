# for i in range(0, 3, 1):
#    for j in range(0, 2, 1):
#        print("변수의 변화를 확인 : ", i, j)

# for dan in range(2, 10):
#    print("%d 단" % dan)
#    for k in range(1, 10):
#        print("%d X %d = %d" %(dan, k, dan*k))
#for i in range(2, 10):
#    print(" %d 단" %i,end= " ")
#print("")    
#for dan in range(2, 10):
#    print("%d 단" % dan)
#    for k in range(1, 10):
#        print("%d X %d = %d" %(dan, k, dan*k))
#for i in range(2, 10):
#    print(" %d 단" %i,end='')
#print("")    
#for k in range(1, 10):
#    #print("%d 단" % dan)
#    for dan in range(2, 10):
#        print("%2dX%2d=%2d " %(dan, k, dan*k), end='')
#    print()


for k in range(10, 1):
    #print("%d 단" % dan)
    for dan in range(10, 2):
        print("%dX%d=%d " %(dan, k, dan*k), end='')
    print()