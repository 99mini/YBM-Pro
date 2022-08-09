#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    col, row = int(ord(pos[0]) - ord('A')), int(pos[1])-1
    dc = [-2,-2,-1,-1,1,1,2,2]
    dr = [1,-1,2,-2,2,-2,1,-1]

    answer = 0

    for i in range(8):
        nc, nr = col + dc[i], row + dr[i]
        if 0 < nc < 8 and 0 < nr < 8:
            answer += 1

    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")