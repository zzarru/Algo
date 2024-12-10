function solution(num1, num2) {
    const remain = num1 % num2
    var answer = (num1 - remain) / num2;
    return answer;
}