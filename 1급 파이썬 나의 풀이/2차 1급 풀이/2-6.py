#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    # 여기에 코드를 작성해주세요.
    answer = [0,0]
    commands_case = ['L','R','U','D']
    for case in commands_case:
        count = str(commands).count(case)
        if case == 'L':
            answer[0] -= count
        elif case == 'R':
            answer[0] += count
        elif case == 'U':
            answer[1] += count
        else:
            answer[1] -= count
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")