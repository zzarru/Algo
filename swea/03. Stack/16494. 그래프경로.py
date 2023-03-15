def searchPath(s, g):
    stack = [s] # 일단 출발지점 stack에 넣고 시작한다.

    while stack: # stack에 값이 있을 때까지 반복한다 -> stack이 비면 while문 탈출
        top = stack.pop() # stack의 마지막값 꺼내주고

        if not visited[top]: # 방문한 적 없으면
            visited[top] = True # 방문했다고 표시해줘라

        for i in range(len(matrix[top])): # top행에 가서 인접노드 찾아라
            if matrix[top][i] == 1 and not visited[i]: # 인접노드 찿고, 그 노드에 방문한 적 없으면
                if i == g: # 근데 그 인접노드가 내가 가려는 도착지점이면
                    return 1 # 경로 찾았으니까 1을 출력하고 while문 탈출! 안녕히 계세요~~
                stack.append(i) # stack에 넣어줘 -> while문 반복

    return 0 # while문 다 돌았는데 경로 없으면 0을 출력해

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())

    # 간선정보 나타내는 방향성 그래프 만들기(인접행렬)
    matrix = [[0]*(V+1) for _ in range(V+1)] # 노드가 1부터 시작하므로 V+1만큼 생성한다. (0 포함)
    for _ in range(E):
        f, t = map(int, input().split())
        matrix[f][t] = 1

    # 방문여부 리스트
    visited = [False]*(V+1)

    # 노드 시작점과 도착점
    s, g = map(int, input().split())

    print(f'#{test} {searchPath(s, g)}')