# 내가 제출한 코드
id = input()
question = '??!'
print(id+question)

# 원래 구현하려던 코드
id = input()
print(id + '??!') #변수명 id 쓰고 바로 + '문자열' 프린트해도 된다.

# 다음엔 이렇게 풀어보자
print(input() + '??!')

'''
어차피 input이 문자열로 들어오기 때문에 + 연산자를 통해서 바로 문자열을 합칠 수 있다!
'''