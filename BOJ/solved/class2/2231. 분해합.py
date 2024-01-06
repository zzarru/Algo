N = int(input())

for i in range(1, N+1):
    # 각 자릿수 합 구하기
    m = sum(map(int, str(i)))
    M = i + m

    # 생성자 최솟값 찾으면 출력하고 for문 정지
    if M == N:
        print(i)
        break
    # 생성자가 없으면 0 출력
    if i == N:
        print(0)