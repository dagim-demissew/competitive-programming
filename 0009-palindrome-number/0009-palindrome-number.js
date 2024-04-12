var isPalindrome = function(x) {
    let str = x.toString().split('');
     let output;
    for(i = 0; i<str.length; i++){
        let a = i;
        let b = str.length - 1 - i
        if(str[a] === str[b]){
            output = true;
        }else{
            output = false;
            break;
        }
    }
   
    return output;
};