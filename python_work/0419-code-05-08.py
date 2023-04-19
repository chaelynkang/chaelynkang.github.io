score = int(input("점수를 입력하세요 : "))

'''
if score >= 60 :
    res= '합격'
else :
    res = '불합격'
'''

res = '합격' if score >= 60 else '불합격'    
print(res)