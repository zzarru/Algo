function solution(s1, s2) {
    var answer = 0;
    s1.forEach((number) => {
        const same = s2.find((el) => el == number)
        if(same == number){answer += 1}
    })
    return answer;
}