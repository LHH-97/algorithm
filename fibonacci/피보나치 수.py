#Lv2 피보나치 수

import sys
sys.setrecursionlimit(10 ** 6)

dic = {0:0,1:1}
def solution(n):
    if n in dic:
        return dic[n]
    dic[n] = (solution(n-1)%1234567 + solution(n-2)%1234567)%1234567
    return dic[n]

#재귀호출 깊이 제한을 늘려주는 코드(파이선의 기본 제귀깊이 설정은 1000이라고 한다.)
import sys
sys.setrecursionlimit(10 ** 7)

#모듈러 연산의 성질. 
#(A+B)%C = (A%C + B%C)%C