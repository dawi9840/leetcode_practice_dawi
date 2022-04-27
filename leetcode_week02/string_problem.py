def defangIPaddr(address:str):
    """ 1108. Defanging an IP Address
    :type address: str
    :rtype: str
    
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    ------------------------
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1" 
    ------------------------
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"
    ------------------------
    Constraints: The given address is a valid IPv4 address.      
    """
    return address.replace(".", "[.]")


def numJewelsInStones(jewels: str, stones: str) -> int:
    ''' 771. Jewels and Stones
    You're given strings jewels representing the types of stones that are jewels, and 
    stones representing the stones you have. Each character in stones is a type of stone you have. 
    You want to know how many of the stones you have are also jewels.
    Letters are case sensitive, so "a" is considered a different type of stone from "A".
    ------------------------
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
    ------------------------
    Input: jewels = "z", stones = "ZZ"
    Output: 0
    ------------------------
    Constraints: 
        1 <= jewels.length, stones.length <= 50
        jewels and stones consist of only English letters.
        All the characters of jewels are unique.
    '''
    count = 0
    for i in range(0, len(jewels)):
        for j in range(0, len(stones)):
            if(jewels[i] == stones[j]):
                count += 1
    return count


def isMatch(s:str, p:str):
    """ 10. Regular Expression Matching
    :type s: str
    :type p: str
    :rtype: bool
    ------------------------
    Given an input string s and a pattern p, implement regular expression matching with 
    support for '.' and '*'

    where:
        '.' Matches any single character.​​​​
        '*' Matches zero or more of the preceding element.
    
    The matching should cover the entire input string (not partial).
    ------------------------
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by 
    repeating 'a' once, it becomes "aa".
    ------------------------
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
    ------------------------
    Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 30
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to 
    match.
    """
    # https://www.cnblogs.com/grandyang/p/4461713.html
    if not p: return not s
        
    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:]) or first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])


class Reverse:
    ''' 7. Reverse Integer
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed
    32-bit integer range [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    ------------------------
    Example 1:
    Input: x = 123
    Output: 321
    ------------------------
    Example 2:
    Input: x = -123
    Output: -321
    ------------------------
    Example 3:
    Input: x = 120
    Output: 21
    ------------------------
    Constraints: -231 <= x <= 231 - 1
    '''    
    def m1(self, x: int) -> int:
        #  dawi Solution:
        tmp_str_list, tmp_int = [], []
        str_n = str(x)
        if str_n[0] == '-':
            for i in range(len(str_n)-1, 0, -1):
                tmp_str_list.append(str_n[i])
            tmp_int = -int(''.join(tmp_str_list))
        else:
            for i in range(len(str_n)-1, -1, -1):
                tmp_str_list.append(str_n[i])
            tmp_int = int(''.join(tmp_str_list))

        if tmp_int >= -2**31 and tmp_int <=2**31-1:
            return tmp_int
        else:
            return 0

    def m2(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)


class isPalindromeNo9:
    '''9. Palindrome Number
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.
    ------------------------
    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    ------------------------
    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    ------------------------
    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    ------------------------
    Constraints: -2^31 <= x <= 2^31 - 1
    '''
    def m1(self, x: int) -> bool:
        str_x = str(x)
        if str_x[0] == '-':
            return False
        else:
            if str_x[::-1] == str_x:
                return True

    def m2(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])


class isPalindromeNo125:
    ''' 125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
    removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    ------------------------
    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    ------------------------
    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    ------------------------
    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
    ------------------------
    Constraints:
        1 <= s.length <= 2 * 10^5
        s consists only of printable ASCII characters.
    '''
    def m1(self, s: str) -> bool:
        s = s.lower()
        tmp_s = []
        for i in range(0, len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                tmp_s.append(s[i])

        if(tmp_s[::-1] == tmp_s[::1]):
            return True
        else: return False


if __name__ == "__main__":
    # numJewelsInStones(jewels='z', stones='aAAbbxzbb')
    input = "0P" 

