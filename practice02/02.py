#문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

source=list(s)
result=[]
i=0

while True :
    if source[i]=='<' :
        while True :
            if source[i]=='>' :                
                result.append('')
                i+=1
                break
            else :
                result.append('')
                i+=1

    else :
        result.append(source[i])
        i+=1
    if len(source)==i :
        break
        

print(s)
print('-'*30)
for e in result :
    print(e,end='')
