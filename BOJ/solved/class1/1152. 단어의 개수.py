'''
1) 공백을 기준으로 단어를 구분한다 -> split() 사용하여 단어 단위로 리스트에 넣어주기
2) len 함수를 이용하여 리스트의 길이 출력 == 단어의 개수
'''
letters = list(map(str, input().split()))
print(len(letters))