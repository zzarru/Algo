// numbers 배열에 있는 값을 순회하면서 다 더해준 뒤, 배열의 길이로 나눠주면 된다.

function solution(numbers) {
    var total = 0;
    var len = numbers.length;
    numbers.forEach((number) => total += number)
    return total / len;
}