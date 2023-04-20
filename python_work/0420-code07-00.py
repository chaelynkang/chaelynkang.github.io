aa = [10, 20, 30]
aa[1:2] = [50, 60]
print(aa)
aa[1:3] = [100, 200]
print(aa)
aa[1] = [22, 33]
print(aa)
del(aa[1])
print(aa)
aa[1:3] = []
print(aa)


