from leetcode_week01.warm_up import add_digits, fizz_buzz, judgeCircle
from leetcode_week01.warm_up import PowerOf, rand
from leetcode_week02.string_problem import defangIPaddr, numJewelsInStones, isMatch
from leetcode_week02.string_problem import Reverse, isPalindromeNo9, isPalindromeNo125


def test_leetcode(n:int):
    print(f'\n[Leecode {n}]')

    leetcode_number =[
        258, 412, 657, 231, 326, 342, 1780, 470,
        1108, 771, 10, 7, 9, 125,
    ]

    for i in range(0, len(leetcode_number)):
        if n != leetcode_number[i]:
            print('Leetcode number not found.')
            break

    # Week 01
    if n == leetcode_number[0]:
        input = 38
        print(f'input: {input}\nresult: {add_digits(input)}')
    if n == leetcode_number[1]:
        input = 15
        fizz_buzz(n=input)
        print(f'[leetcode 412]\ninput: {input}\nresult: {fizz_buzz(input)}')
    if n == leetcode_number[2]:
        input = 'LR'
        print(f'input: {input}\nresult: {judgeCircle(moves=input)}')
    if n == leetcode_number[3]:
        input = 7
        question231 = PowerOf()
        result = question231.isPowerOfTwo(n=input)
        print(f'input: {input}\nresult: {result}')
    if n == leetcode_number[4]:
        input = 27
        question326 = PowerOf()
        result = question326.isPowerOfThree(n=input)
        print(f'input: {input}\nresult: {result}')
    if n == leetcode_number[5]:
        input = 5
        question342 = PowerOf()
        result = question342.isPowerOfFour(n=input)
        print(f'input: {input}\nresult: {result}')
    if n == leetcode_number[6]:
        # 12, 91, 21
        # true, true, false
        input = 21
        test1780 =  PowerOf()
        result = test1780.checkPowersOfThree(n=input)
        print(f'input: {input}\noutput: {result}')
    if n == leetcode_number[7]:
        input = 7
        test470 = rand()
        print(f'input: {input}')
        result = []
        for i in range(0, input):
            result.append(test470.rand10())
        print(f'result: {result}')
    # Week 02
    if n == leetcode_number[8]:
        input = "1.1.1.1"
        print(f'input: {input}\nresult: {defangIPaddr(address=input)}')    
    if n == leetcode_number[9]:
        in_str1, in_str2 = 'za', 'aAAbbxzbb'
        out = numJewelsInStones(jewels=in_str1, stones=in_str2) 
        print(f'input1: {in_str1}, intput2: {in_str2}\nresult: {out}')
    if n == leetcode_number[10]:
        # str1, str2 = "mississippi", "mis*is*p*."
        str1, str2 = "az", "a*cvb"
        print(f'Input1: {str1}, Input2: {str2}')
        print(f'output:{isMatch(s=str1, p=str2)}')
    if n == leetcode_number[11]:
        input = -1263
        # input = 1534236469
        test7 = Reverse()
        leetcode7_m1 = test7.m1(x=input)
        leetcode7_m2 = test7.m2(x=input)
        print(f'input: {input}')
        print(f'output m1: {leetcode7_m1}\noutput m2: {leetcode7_m2}')
    if n == leetcode_number[12]:
        input = 121
        test9 = isPalindromeNo9()
        m1 = test9.m1(x=input)
        m2 = test9.m2(x=input)
        print(f'input: {input}')
        print(f'm1 output: {m1}\nm2 output: {m2}')
    if n == leetcode_number[13]:
        # input = 'race a car'
        # input = 'pp a p, pd'
        input = "Marge, let's \"[went].\" I await {news} telegram." # True
        # input = "0P" # False
        test125 = isPalindromeNo125()
        print(f'Input: {input}\noutput isPalindrome: {test125.m1(s=input)}')
    

def continuity_manual_test():
    print('leetcode number for test.')
    while True:
        print('-'*40)
        leetcode_number = int(input('key number:'))
        if leetcode_number == 0: 
            break
        else: 
            test_leetcode(n=leetcode_number)


if __name__ == '__main__':
    # test_leetcode(9)
    continuity_manual_test()

    