#1 내가 제출한 코드
A, B = map(str, input().split())

a = ''
for i in A[::-1]:
    a += i
b = ''
for j in B[::-1]:
    b += j

a = int(a)
b = int(b)

if a > b:
    print(a)
else:
    print(b)

#2 수정 코드
A, B = input().split() # 굳이 mapping할 필요없다. ; map은 리스트의 요소를 함수로 처리해주는 함수!
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)


#3 삼항 연산자 활용 코드
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

print(A) if A > B else print(B)