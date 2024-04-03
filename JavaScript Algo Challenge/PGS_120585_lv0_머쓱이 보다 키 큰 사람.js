function solution(array, height) {
    var cnt = 0
    array.forEach((student) => {
        if (student > height){
            cnt += 1
        }
    })
    return cnt;
}