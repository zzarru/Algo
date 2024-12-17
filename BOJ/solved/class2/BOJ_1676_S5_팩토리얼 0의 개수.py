# 1. 팩토리얼 함수 만들기
def factorial(n):
    ans = 1
    while n != 0:
        ans *= n
        n -= 1
    return ans


# 2. 0이 아닌 숫자가 오는 위치 확인하기
N = int(input())
str_fac = str(factorial(N)) # 문자열로 변환
pointer = len(str_fac) # 문자열 길이 구하기

# 뒤에서 부터 문자열 검사 (0이 아닌 숫자가 나올 때까지)
while pointer > 0:
    pointer -= 1
    if str_fac[pointer] == '0':
        continue
    else:
        break

# 문자열 길이 - 0이 아닌 숫자 위치
print(len(str_fac) - pointer - 1)

'''
1. 팩토리얼 함수를 만든다. 
2. N!을 문자열로 바꾸어 0이 아닌 숫자가 나오는 위치를 파악한다.
 1) 문자열로 바꾸기
 2) 뒤에서부터 검사하기 위한 포인터를 만든다. 
'''
