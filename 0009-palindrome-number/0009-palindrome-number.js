/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str = x.toString().split('');
    let reverse = [];
    for (let i = str.length - 1; i >= 0; i--) {
        reverse.push(str[i]);
    }
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === reverse[i]) {
            count++;
        } else {
            count = 0;
        }
    }
    let output;
    if (count === x.toString().length) {
        output = true;
    } else {
        output = false;
    }
    return output;
};