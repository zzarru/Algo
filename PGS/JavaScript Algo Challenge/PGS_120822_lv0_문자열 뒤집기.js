function solution(my_string) {
    var answer = ''
    var leng = my_string.length
    for (i = 0; i < leng; i++){
        answer += my_string[leng-i-1]
    }
    return answer;
}