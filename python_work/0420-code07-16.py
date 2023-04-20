# 딕셔너리
student1 = {'학번': 1000, '학번':200,'이름':'홍길동', '학과':'컴퓨터학과', '주소':'서울특별시 관악구 봉천동 304가길'}
print(student1)

# 추가
student1['연락처'] = '010-1234-1234'
print(student1)

student1['학과'] = '파이썬학과'
print(student1)

del(student1)['학과']
print(student1)

print(student1['학번'])
print(student1['이름'])
print(student1['연락처'])

print(student1.get('학번')) #get 함수로도 불러올 수 있다.
print(student1.get('주소'))

print(student1.keys()) # keys 함수로 keys에 해당되는 것만 불러옴.
print(list(student1.keys())) # list로 가져올 수 있음.

print(student1.values()) # values로 가져옴.
print(student1.items()) # items로 몽땅 가져옴.
print(list(student1.values()))
print(list(student1.items())) # 튜플을 리스트로 몽땅 가져옴.

print('이름' in student1)
print('학년' in student1) # 없어서 false로 알려줌. 

for i in student1.keys() :
    print('%s ======> %s' %(i, student1[i])) #for문의 i를 활용하여 해당하는 내용을 뽑아 올 수 있음.
