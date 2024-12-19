# 1. 점들의 좌표를 (x, y) 튜플 형태로 저장
dots = []
for _ in range(int(input())):
    dots.append(tuple(map(int, input().split())))

# 2. y 좌표 오름차순으로 정렬한 뒤, x 좌표 오름차순으로 정렬
sorted_dots = sorted(dots, key=lambda x: (x[1], x[0]))

# 3. 공백을 두고 좌표 출력
for dot in sorted_dots:
    print(*dot)
