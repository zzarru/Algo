function solution(n) {
    var pizza = 0;
    var remain = n % 7;
    if (remain != 0){
        pizza = ((n - remain) / 7) + 1
    } else {
        pizza = n / 7
    }
    return pizza;
}