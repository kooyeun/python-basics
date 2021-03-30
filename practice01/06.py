#키보드에서 정수로 된 돈의 액수를 입력 받아
#오만 원권, 만원 권, 오천 원권, 천원 권,
#500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
#각 몇 개로 변환 되는지 작성하시오

money=int(input("금액 : "))

c50000=0
c10000=0
c5000=0
c1000=0
c500=0
c100=0
c50=0
c10=0
c5=0
c1=0
temp=money

if temp>=50000 :
    c50000=temp//50000
    temp=temp%50000
if temp>=10000 :
    c10000=temp//10000
    temp=temp%10000
if temp>=5000 :
    c5000=temp//5000
    temp=temp%5000
if temp>=1000 :
    c1000=temp//1000
    temp=temp%1000
if temp>=500 :
    c500=temp//500
    temp=temp%500
if temp>=100 :
    c100=temp//100
    temp=temp%100
if temp>=50 :
    c50=temp//50
    temp=temp%50
if temp>=10 :
    c10=temp//10
    temp=temp%10
if temp>=5 :
    c5=temp//5
    temp=temp%5
if temp>=1 :
    c1=temp//1

print("\n50000원 : %d개"%c50000)
print("10000원 : %d개"%c10000)
print("5000원 : %d개"%c5000)
print("1000원 : %d개"%c1000)
print("500원 : %d개"%c500)
print("100원 : %d개"%c100)
print("50원 : %d개"%c50)
print("10원 : %d개"%c10)
print("5원 : %d개"%c5)
print("1원 : %d개"%c1)

