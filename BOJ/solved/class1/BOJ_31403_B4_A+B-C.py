#0 입력받기 (정수)
A = int(input())
B = int(input())
C = int(input())

#1 정수로 생각하기
print(A+B-C)

#2 문자열로 생각하기
strAB = str(A) + str(B)
intAB = int(strAB)
print(intAB-C)


'''
1) input() -> 문자열로 입력을 받음
2) print문 안에서 함수를 int(), str() 함수를 바로 썼다면 코드가 간결해졌을 거 같다.
ex)
A = input() #문자열
B = input() #문자열
C = int(input()) #정수

#1 정수로 계산
print(int(A)+int(B)-C)

#2 문자열로 계산
print(int(A+B)-C))
'''