#1 내가 작성한 코드
numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)

mx = max(numbers)
mx_idx = numbers.index(mx) + 1

print(mx)
print(mx_idx)

#2 print 안에 바로 함수를 사용한 경우
numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)

#2 참고 코드
# numbers = [int(input()) for _ in range(9)] # list comprehension을 이용한 코드
#
# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)