# CodeUp 1905번 에 의한 전역,지역 변수 정리

def f(n):
    global sum
    print(sum)
    sum = n
    return sum
sum = 9
print(f(int(input())))
print(sum)

'''
함수안에서 만들어진 변수를 지역 변수라 하고, 함수 밖에서 만들어진 변수를 전역 변수라 한다. 
지역변수는 해당 함수의 실행이 끝나면 없어지고, 전역변수는 스크립트 파일의 실행이 끝나면 전역 프레임과 함께 사라진다.(파이썬 코딩도장 참조)

global을 통해 해당 sum 변수를 전역변수로 사용해주겠다라고 명시하였다. 그렇기에 print(sum) 값이 9가 출력된다.
global 키워드를 사용해주지 않으면, UnboundLocalError: local variable 'sum' referenced before assignment와 같이 에러가 발생하게 된다. 

'''