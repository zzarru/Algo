"""
문제 해결 아이디어
1. 입력으로 3개의 문자열이 주어진다.
 1) 3과 5의 배수는 연속하여 나타나지 않기 때문에 주어지는 입력 중에 반드시 '정수'가 포함된다.
 2) 입력 받은 연속된 문자열 3개 중에서 '정수'가 나타나는 위치를 파악하여, 그 다음 올 문자열이 무엇인지 파악한다.

2. FizzBuzz라는 리스트를 만들고 입력 받은 문자열 중 '정수'가 어디에 위치해 있는지 확인한다.
 1) input() 받으면 문자열로 입력을 받기 때문에, 정수인지 아닌지 파악한다.
 2) 해당 정수 + 파악한 정수 위치를 통하여 다음에 올 문자열을 파악한다.

3. 그 다음에 올 문자열이 3의 배수, 5의 배수인지 아닌지 판단하여 조건에 맞게 출력한다.
"""

#1 입력 받기
FizzBuzz = []
for _ in range(3):
    numbers = '0123456789' # 정수인지 아닌지 판별하기 위한 문자열
    str = input() # input()은 문자열로 입력을 받는다.
    if str[0] in numbers: # 입력받은 문자열이 정수인지 아닌지 파악하기 위하여 str[0]을 활용
        str = int(str) # 정수라면 int로 변환하여 리스트 저장
        FizzBuzz.append(str)
    else:
        FizzBuzz.append(str)

#2 정수 위치 파악하기
next_str = 0
for i in FizzBuzz:
    if type(i) == int: # 정수인지 아닌지 파악
        next_str = i + (3- FizzBuzz.index(i))
        break # 이미 정수의 위치를 파악했다면 다음 정수의 위치는 굳이 탐색하지 않아도 됨
    else:
        continue

#3 조건에 따라 다음 문자열 출력하기
if next_str % 3 == 0:
    if next_str % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")

else:
    if next_str % 5 == 0:
        print("Buzz")
    else:
        print(next_str)