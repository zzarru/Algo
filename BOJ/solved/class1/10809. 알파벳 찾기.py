#1 내가 제출한 코드
alpha_dic = {
    'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1
}

S = input()
for s in S:
    if alpha_dic[s] == -1:
        alpha_dic[s] = S.index(s)


print(*(alpha_dic.values()))

#2 for 문 이용하기
S = input()
alpah = 'abcdefghijklmnopqrstuvwxyz'

ans = ''
for a in alpah:
    if a in S:
        ans += (str(S.index(a))+ ' ')
    else:
        ans += ('-1' + ' ')

print(ans)

#3 end=' ' 를 사용하여 코드 정리하기
S = input()
alpah = 'abcdefghijklmnopqrstuvwxyz'

for a in alpah:
    if a in S:
        print(S.index(a), end=' ')
    else:
        print(-1, end= ' ')