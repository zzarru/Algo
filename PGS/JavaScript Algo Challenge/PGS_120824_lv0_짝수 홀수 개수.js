function solution(num_list) {
    var odd = 0;
    var even = 0;
    num_list.forEach((number) => {if(number % 2){
        odd += 1
    }else{
        even += 1
    }})
    return [even, odd];
}