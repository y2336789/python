def solution(n):
    answer = 0
    data = []
    while True:
        if n != 1:
            a = n % 3
            n //= 3
            data.append(a)
        else:
            data.append(1)
            break
    for i in range(len(data)-1, -1, -1):
        answer += data[i] ** (len(data)-1 - i)
    return answer

    # def solution(n):
    # answer = ''
    # while n >= 1:
    #     a = n % 3
    #     n //= 3
    #     answer += str(a)

    # return int(answer, 3) -> int(n, base)를 통해 n 문자열을 base진법으로 변환후 int로 출력