/*
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let str = x.toString();
    const isNegative = str[0] === "-"
    str = isNegative ? str.substring(1) : str;
    
    let ret = "";
    for (let i = str.length - 1; i >= 0; --i) {
        ret += str[i];
    }
    
    ret = isNegative ? "-" + ret : ret;
    ret = parseInt(ret, 10);
    ret = (ret < -(2**31) || ret > (2**31 - 1)) ? 0 : ret;
    
    return ret;
};