#문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서
#       각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

print(s)

if s[0:1]=='/' :
    slisingS=s[1:]
    splitStr=slisingS.split('/')
    print(splitStr)
else :    
    splitStr=s.split('/')
    print(splitStr)
