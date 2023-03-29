'''
내가 푼 거 아님.. 다시 풀어야댐
1) 신청서 - 작업 끝나는 시간 순으로 정렬하기 (오름차순)
2) 끝나는 시간이랑 다음 신청서의 시작하는 시간이 겹치지 않으면 cnt += 1
3) 작업 끝난 시간 업뎃해주기
'''
T = int(input())
for test in range(1, T+1):
    N = int(input())
    times = []
    for _ in range(N):
        start, end = map(int, input().split())
        times.append((start,end))

    times.sort(key=lambda x:x[1])

    cnt = 0
    end_time = 0
    for s, e in times:
        if end_time <= s:
            cnt += 1
            end_time = e

    print(f'#{test} {cnt}')