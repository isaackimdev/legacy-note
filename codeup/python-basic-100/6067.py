'''

본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.

예시
...
if n<0 :
  if n%2==0 :
    print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')
...

참고
조건/선택 실행구조 안에 다시 조건/선택 실행구조를 "중첩"할 수가 있다.

또한, 중첩된 조건은
...
if (n<0) and (n%2==0) :
    print('A')
...
와 같이 논리연산자(not, and, or)를 이용해 합쳐 표현할 수도 있다.
비교연산(<, >, <=, >=, ==, !=) 의 계산 결과는 True 또는 False 의 불(boolean) 값이고,
불 값들 사이의 논리연산(not, and, or)의 결과도 True 또는 False 의 불 값이다.

'''
n=int(input())
if n < 0 :
    if n % 2 == 0 :
        print('A')
    else :
        print('B')
else :
    if n % 2 == 0 :
        print('C')
    else :
        print('D')