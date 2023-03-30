#1 내 코드
N = int(input())
numbers = list(map(int, input())) #리스트에 정수로 저장한다. int는 iterable한 객체가 아니므로

total = 0
for number in numbers:
    total += number

print(total)

#2 
N = int(input())
numbers = input() #문자열로 받아준다. str은 iterable한 객체이므로 for문으로 바로 넘겨받을 수 있음.

total = 0
for number in numbers:
    total += int(number) #인자를 넘겨 받을 때 형변환(str->int)을 해주고 바로 더한다. 

print(total)