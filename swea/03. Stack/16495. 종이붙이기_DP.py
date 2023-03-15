T = int(input())
for test in range(1, T+1):
    N = int(input())
    N = N//10

    def paper(N):
        # paper 리스트에 값을 계속 저장해줌으로써 memoization사용..?
        paper = [0] * (N + 2) # 길이가 0인 것을 제외했기 때문에 N+2해줌.. 두개의 값을 미리 할당할 것이기 때문에
        paper[1] = 1
        paper[2] = 3
        for i in range(3, N + 1): # 이미 1, 2인 경우는 지정해주었기 때문에 3부터 구한다.
            paper[i] = paper[i - 1] + (paper[i - 2] * 2) # 왜 이런 규칙인지는 모르겠음.. 걍 DP다..

        return paper[N]

    print(f'#{test} {paper(N)}')