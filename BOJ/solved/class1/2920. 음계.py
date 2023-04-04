#1 내가 제출한 코드
scale = int(''.join(input().split()))

if scale == 12345678:
    print('ascending')
elif scale == 87654321:
    print('descending')
else:
    print('mixed')

#2 굳이 join method를 사용해야할까?
scale = input()

if scale == '1 2 3 4 5 6 7 8':
    print('ascending')
elif scale == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')

#3 리스트와 sort 함수를 쓰는 게 좋을까?
scale = list(map(int, input().split()))

if scale == sorted(scale): #오름차순 정렬
    print('ascending')
elif scale == sorted(scale, reverse=True): # 내림차순 정렬
    print('descending')
else:
    print('mixed')


'''
항상 생각할 것
1) tc가 무한히 늘어난다면?
2) 뒤집어서 생각한다면?

아직은 어떤 코드가 효율적인지 잘 모르겠다. 
'''