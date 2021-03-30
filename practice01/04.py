#다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

for i in range(1,10) :
    for j in range(1,10) :
        print("{0} x {1} = {2}\t".format(j,i,i*j),end="")
    print()
