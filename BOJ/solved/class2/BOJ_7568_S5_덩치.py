N = int(input())
# 1. 사람들의 몸무게와 키 리스트에 저장하기
people = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

# 2. 리스트를 순회하며 나보다 덩치가 큰 사람의 수를 구한다.
grades = []  # 등급 리스트
for i in range(N):
    man = people[i]
    weight = man[0]
    height = man[1]

    grade = 1  # 덩치가 큰 사람 + 1 == 등수
    for person in people:
        if weight < person[0] and height < person[1]:
            grade += 1
        else:
            continue
    grades.append(grade)

# 3. 출력
for grade in grades:
    print(grade, end=' ')

'''
1. 사람들의 키, 몸무게 정보를 리스트에 담는다.
2. 리스트를 순회하며 자기보다 덩치가 큰(몸무게와 키 모두 수가 커야함) 사람의 수를 센다.
 1) 본인은 어차피 카운트하지 않으므로 비교해도 상관없음. 
 2) 등수는 나보다 (덩치가 큰 사람의 수 + 1) 이다.
3. 출력 시 공백을 두고 출력한다.
'''
