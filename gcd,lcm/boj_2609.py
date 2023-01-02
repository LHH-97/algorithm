# 유클리드 알고리즘을 이용한 코드
def gcd(a,b):
    while(b>0):
        a,b = b,a%b
    return a

a,b = map(int,input().split())
print(gcd(a,b),a*b//gcd(a,b),sep = '\n')

#math 라이브러리를 사용한 코드
import math
a,b = map(int,input().split())
print(math.gcd(a,b),math.lcm(a,b),sep = '\n')