#문제3. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요

str=['After','Available','Contribute','Contributors','.','.','.','.','.','to','we','you']
result=[]

for i in str :
    temp=i.replace(',','')
    temp=temp.replace('.','')
    temp=temp.replace('\n','')
    result.append(temp.upper())

for i in result :
    print(i)
