print("값을 입력하세요 공백을 이용해 여러개의 수를 입력 가능> (가장큰수의 사용횟수, 더하기 반복횟수)")

numMaxRepeat, addRepeatCount = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first  = data[len(data) - 1]
second = data[len(data) - 2]

result = 0

while True:
    for i in range(addRepeatCount):

        if numMaxRepeat == 0:
            break

        result += first
        numMaxRepeat -= 1

    if numMaxRepeat == 0:
        break

    result += second
    numMaxRepeat -= 1

print('결과값 : ', result)