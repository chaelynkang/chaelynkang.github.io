# 튜플
tt1 = (10, 20, 30)
tt2 = 40, 50, 60
print(tt1); print(tt2)
tt3 = 70
print(tt3)
tt4 = (00)
print(tt4)

# 튜플은 읽기 전용
# tt1.append(100) => AttributeError: 'tuple' object has no attribute 'append'
# tt1[0] = 100 => TypeError: 'tuple' object does not support item assignment
# del(tt1[0]) => TypeError: 'tuple' object doesn't support item deletion
del(tt4)
# print(tt4) => error

print(tt1[0]) # 번지 출력 가능
print(tt1[0]+tt2[0]) # 연산가능

print(tt1[:2])
print(tt1[1:2])
print(tt1[1:])

print(tt1 + tt2)
print(tt1 * 3)

tt1List = list(tt1) # 튜플을 리스트로 생성
print(tt1List)
tt1List.append(40)
tt1 = tuple(tt1List) # 리스트로 어펜드 가능하게 하고, 다시 tuple로 .
print(tt1)