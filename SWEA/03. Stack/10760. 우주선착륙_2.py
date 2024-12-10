T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    height_lst = [list(map(int, input().split())) for _ in range(N)]

    # 8방향 델타 탐색 좌표
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    candidate_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]

                # 구역 바깥으로 나가지 않는 범위만 탐색
                if 0 <= ni < N and 0 <= nj < M:
                    if height_lst[i][j] > height_lst[ni][nj]:
                        cnt += 1

            if cnt >= 4:
                candidate_cnt += 1

    print(f'#{test} {candidate_cnt}')