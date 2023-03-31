#1 내 코드 ; max, min 메서드 사용하기
N = int(input())
nums = list(map(int, input().split()))
mx = max(nums)
mn = min(nums)
print(mn, mx)

#2 두번째 방법 ; 매서드 사용않고 최대, 최소 구하기
N = int(input())
mx = -10000000
mn = 1000000
for num in input().split(' '):
    if int(num) > mx:
        mx = int(num)
    if int(num) < mn:
        mn = int(num)

print(mn, mx)

'''
N이 사용되지 않는데.. 이걸 사용하는 방법은 없을까?
'''
N = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for i in range(N):
    if int(nums[i]) > max_num:
        max_num = nums[i]
    if int(nums[i]) < min_num:
        min_num = nums[i]
print(min_num, max_num)

'''
참조
https://velog.io/@devheyrin/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-10818-%EC%B5%9C%EB%8C%80-%EC%B5%9C%EC%86%8C

딱히... 코드 자체의 문제는 아니엇던 거 같음. 백준 자체가 테케가 엄청 많나보다...테케가 많든 테케의 입력값이 엄청 크거나!
'''