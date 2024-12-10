function solution(my_string, letter) {
    var del_str = my_string.replaceAll(letter, '')
    return del_str;
}