T = 1
for test in range(1, T+1):
    tc = int(input())
    word = input()
    letters = input()

    cnt = 0
    for i in range(len(letters)-len(word)+1): # 범위 설정!!!!!!
        if word == letters[i:i+len(word)]:
            cnt += 1

    print(f'#{tc} {cnt}')