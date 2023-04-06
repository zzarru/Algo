#1 처음 제출한 코드 (오답)
while True:
    a, b, c = map(int, input().split())
    if a and b and c !=0:
        if c**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')

    else:
        break

#2 수정한 코드 (정답)
while True: #input이 있는동안 계속 반복한다.
    triangle = list(map(int, input().split()))
    triangle.sort() #리스트 정렬(오름차순); triangle = triangle.sort() 이렇게 적으면 안됨..
    if sum(triangle) != 0: # 맨 마지막으로 들어오는 input이 0 0 0 이라고 했으므로
        if triangle[2]**2 == triangle[0]**2 + triangle[1]**2: # 가장 큰 값의 제곱과 나머지 두 변의 제곱의 합이 같으면 직각삼각형
            print('right')
        else:
            print('wrong')

    else: #input이 없으면 break
        break

#3 리스트 정렬이 아니라 최대값을 찾아서 -> 제거해주는 방식으로
while True:
    triangle = list(map(int, input().split()))
    if 0 not in triangle: # 0 이외의 숫자가 들어있다면 (0 0 0 이 아니라면)
        mx = max(triangle) #가장 길이가 긴 변 구하기
        triangle.remove(mx) # mx를 리스트에서 제거하기
        if mx**2 == triangle[0]**2 + triangle[1]**2:
            print('right')
        else:
            print('wrong')

    else:
        break




'''
input이 몇개 들어오는지 모르는 경우,
input을 어떻게 받아줘야할지.. 모르겠다..흑흑..
근데 왜 블로그 보면 사람들 풀이가 다 똑같지... 다 베껴서 풀엇나...... 아님 나만 모르는 거임?
'''


