try:
    while True: #무한반복
        A, B = map(int, input().split())
        print(A+B)
except: #입력값이 없으면 에러가 뜨니까 except문 작동
    pass