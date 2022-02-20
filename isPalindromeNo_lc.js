/**
 * Determine whether an integer is a palindrome. 
 * An integer is a palindrome when it reads the same backward as forward.
*/



// /**
//  * @param {number} x
//  * @return {boolean}
//  */
// var isPalindrome = function(x) {
//     if(x<0){
//         return false
//     } 
//     if(x<10){
//         return true
//     }

//     let lastDigit = x%10
//     let t = Math.floor(Math.log10(x))
//     let firstDigit = Math.floor(x/(10**t))
//     if (firstDigit != lastDigit){
//         return false 
//     } else{
//         x=x-firstDigit*(10**t)
//         console.log(x)
//         x=Math.floor(x/10)
//         console.log(x)        
//         return isPalindrome(x)
//     }
    
// };


/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let y=x
    let z=0
    while(y!=0){
        z=10*z+y%10
        y=Math.floor(y/10)
    }
    console.log(x,z)
    if (x==z){
        return true
    } else {
        return false
    }

};



let x=43210000123
x=123123123
// let t = Math.log10(x)
// t=Math.floor(t)
// console.log(t)
// console.log(x, 10**t,10^t)
// console.log(Math.floor(x/(10**t)))

console.log('-------------------------')
console.log(isPalindrome(x))
