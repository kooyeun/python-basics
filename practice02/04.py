#문제4. 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
#출력해보세요. 1부터 99까지만 실행하세요



for i in range(1,100) :
    word=str(i)
    hands=''
    for j in word :
        if j=='3' or j=='6' or j=='9' :
            hands+='짝'
    print('%d\t%s'%(i,hands))
        
        


