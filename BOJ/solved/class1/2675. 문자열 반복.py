#1 최초 내가 제출한 코드
for _ in range(int(input())):
    R, letters = input().split()
    R = int(R)

    letter_lst = list(map(str, letters))

    P = '' # 문자열 합치기의 원리를 이용하기
    for letter in letter_lst:
        P += letter * R

    print(P)

#2 수정한 코드
for _ in range(int(input())):
    R, letters = input().split()
    R = int(R)

    P = '' # 문자열 합치기의 원리를 이용하기
    for letter in letters: # 문자열 자체로 순회 가능하므로 리스트를 따로 만들 필요가 없다.
        P += letter * R

    print(P)