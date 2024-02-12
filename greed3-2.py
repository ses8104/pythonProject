print("값을 입력하세요 공백을 이용해 여러개의 수를 입력 가능> (가장큰수의 사용횟수, 더하기 반복횟수)")

numMaxRepeat, addRepeatCount = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[len(data) - 1]
second = data[len(data) - 2]

result = 0

count = int(numMaxRepeat / (addRepeatCount + 1)) * addRepeatCount
count += numMaxRepeat % (addRepeatCount + 1)

result += count * first
result += (numMaxRepeat - count) * second

print(f"결과값 : {result}")
# # # # # # # # # # # # # # # # # # # # # #
# 값을 입력하세요 공백을 이용해 여러개의 수를 입력 가능> (가장큰수의 사용횟수, 더하기 반복횟수)
# 8 3
# 2 4 5 4 6
# 결과값 :  46
#
# Process finished with exit code 0
# # # # # # # # # # # # # # # # # # # # # #
