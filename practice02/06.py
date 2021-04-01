import random
import sys

#num=random.randrange(1,101)
#print('수를 결정하였습니다.맞추어 보세요\n1-100')

def chooseNum() :
    randNum = random.randrange(1, 101)
    print('-'*30)
    print('수를 결정하였습니다.맞추어 보세요\n1-100')
    print(randNum)

    count=1
    while True :
        userNum = input(str(count) + '>>')
        if randNum == int(userNum) :
            print('맞았습니다')
            question=input('다시 하시겠습니까(y/n)>>')
            if question=='n' or question=='N' :
                print('\t--<< 게임 종료 >>--')
                sys.exit(0)
            elif question=='y' or question=='Y' :
                return chooseNum()
        else :
            if userNum < randNum :
                print('더 높게')






chooseNum()