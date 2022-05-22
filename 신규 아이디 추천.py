def solution(new_id):
    # 1단계 파라미터로 받아온 new_id를 소문자로 바꾼다.
    new_id = new_id.lower() 
    answer = ''

    for i in new_id: # 2단계 new_id 속 문자 하나하나씩 검사
        if i.isalnum() or i in '-_.': # 숫자, 영어, -, _, .인 경우에만
            answer += i
        
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계 
    if answer and answer[0] == '.': # answer가 비어있는 문자열일 수도 있기에 확인
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer