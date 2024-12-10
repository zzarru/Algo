def navigator(s,e):
    stack = [s] # 일단 시작점 stack에 넣음
    while stack: # stack에 값이 있는 동안 계속 반복된다..
        v = stack.pop() # stack의 마지막 요소 꺼내
        if not visited[v]: # 방문한 적 없으면
            visited[v] = True # 방문했다고 표시해

        for i in range(len(matrix[v])): # 방문한 곳의 인접행렬을 찾아
            if matrix[v][i] == 1 and not visited[i]: # 방문한 적 없고
                if i == e: # 도착지점이면 경로 있으니까 1을 반환해 그리고 while 탈출
                    return 1
                stack.append(i) # 도착지점 아니면 stack에 넣어 -> 무한 while문으로 다시 가
    return 0 # stack에 남은 값이 없어서 while문 탈출했는데 경로 못찾았으면 0을 반환한다.

T = 10
for i in range(T):
    test, M = map(int, input().split())
    lst = list(map(int, input().split())) # 일단 인접 정보가 한줄로 되어있기 때문에 리스트로 받는다.
    matrix = [[0]*100 for _ in range(100)] # 시작점 0부터 도착점 99까지 총 100개...
    visited = [False]*100 # 방문유무 표시해야됨..

    s = 0 # 시작점(A도시)은 0으로 고정
    e = 99 # 도착점(B도시)은 99로 고정

    # 인접행렬 만들기
    for i in range(M):
        f, t = lst[i*2], lst[i*2+1] # 리스트에 있는 값을 두개씩 받아줄 거임
        matrix[f][t] = 1 # 한방향

    print(f'#{test} {navigator(s, e)}')

