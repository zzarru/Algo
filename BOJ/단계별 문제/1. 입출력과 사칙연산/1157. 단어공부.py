'''
1) 문자열 입력받을 때 대문자로 받기 : upper() 메서드 사용
2) 문자열을 구성하고 있는 알파벳 리스트 만들기 : lst
3) lst에 있는 알파벳이 문자열에 몇개있는지 세기 : str.count() 메서드 사용
4) 가장 많이 사용된 알파벳의 개수 구하기 : mx = max(cnt_lst)
5) mx값을 가진 알파벳 구하기 : mx_lst
'''
#1 대문자로 문자열 입력 받기
letters = input().upper()

#2 문자열 구성하고 있는 알파벳 리스트 만들기
lst = []
for letter in letters:
    if letter not in lst:
        lst.append(letter)

#3 각 알파벳이 문자열에 몇개 있는지 세기
cnt_lst = []
for i in lst:
    cnt = letters.count(i)
    cnt_lst.append(cnt)

#4 가장 많이 사용된 알파벳의 개수 = mx
mx = max(cnt_lst)

#5 가장 많이 사용된 알파벳 리스트 만들기
mx_lst = []
for j in range(len(cnt_lst)):
    if mx == cnt_lst[j]:
        mx_lst.append(lst[j])

#6-1 가장 많이 사용된 알파벳이 2개 이상일 경우 '?' 출력
if len(mx_lst) > 1:
    ans = '?'
#6-2 가장 많이 사용된 알파벳이 1일 경우, 그 알파벳 출력(대문자) -> 이걸 좀더 간단히 하는 방법은 없을까
else:
    ans = ''.join(mx_lst)

print(ans)