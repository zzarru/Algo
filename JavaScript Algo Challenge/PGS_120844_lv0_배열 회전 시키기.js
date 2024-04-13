function solution(numbers, direction) {
    if (direction == 'right') {
        const pop = numbers.pop()
        const new_numbers = []
        new_numbers.push(pop)
        new_numbers.push(...numbers)

        return new_numbers
    } else {
        const shift = numbers.shift()
        numbers.push(shift)
        return numbers;
    }
}