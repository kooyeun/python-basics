#문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수
#reverse(s)을 작성하세요

source=list(input("입력> "))
source.reverse()
print("\n결과> ",end="")
for i in source :
    print(i,end="")
