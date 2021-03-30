#키보드에서 5개의 정수를 입력 받아 리스트에 저장하고
#평균을 구하는 프로그램을 작성하시오

list=[]
sum=0

for i in range(5) :
    list.append(int(input(">")))
    sum+=list[i]

print("평균 : %.1f"%(sum/5))
