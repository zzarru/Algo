def solution(s):
    answer = True
    brackets = []
    for bracket in s:
        if bracket == "(":
            brackets.append(bracket)

        else:  # bracket == ")"
            if brackets:  # 안비어있으면
                brackets.pop()
            else:  # 비어있으면
                answer = False
                break

    if brackets:  # brackets 검사해서 여는 괄호가 남아있다면 False
        answer = False
    else:
        pass

    return answer