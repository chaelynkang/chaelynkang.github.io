aa = []
bb = []
value = 0

for i in range(0, 100) :
    aa.append(value)
    value += 2
print(aa)
for i in range(0, 100) :
    bb.append(aa[99 - i])

print("-"*100)
print(bb)
