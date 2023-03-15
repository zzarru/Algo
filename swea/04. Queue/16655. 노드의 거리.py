# 최소간선 구하는 함수 만들기
def minRoute(graph, start, goal):
    visited = [0]*(V+1)
    queue = []
    queue.append(start)
    visited[start] = 1

    while queue:
        step = queue.pop(0)

        for next in graph[step]:
            if not visited[next]:
                queue.append(next)
                visited[next] = visited[step] + 1

    # 결과값 리턴
    if visited[goal] == 0: # start와 goal이 연결되어 있지 않은 경우
        return 0

    else: # start와 goal이 연결되어 있는 경우
        return visited[goal] - 1

#input 받기
T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())

    # 인접리스트 만들기 (양방향 그래프)
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)

    start, goal = map(int, input().split())

    print(f'#{test} {minRoute(graph, start, goal)}')