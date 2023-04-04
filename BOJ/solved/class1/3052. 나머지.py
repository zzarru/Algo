#1 내가 제출한 코드
remains = []
for _ in range(10):
    num = int(input())
    remain = num % 42
    if remain not in remains:
        remains.append(remain)

print(len(remains))

#2 set() 함수를 이용한 코드 ; set 함수가 뭔지 공부하기
remains = []
for _ in range(10):
    num = int(input())
    remains.append((num%42))

remains = set(remains)

print(len(remains))