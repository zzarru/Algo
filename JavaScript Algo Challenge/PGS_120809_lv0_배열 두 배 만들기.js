function solution(numbers) {
    for (i = 0; i < numbers.length; i ++){
        numbers[i] += numbers[i]
    }
    return numbers;
}