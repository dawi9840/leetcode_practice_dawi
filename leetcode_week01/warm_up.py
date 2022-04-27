import random

def add_digits(num: int) -> int:
    ''' 258. Add Digits
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
    ------------------------
    Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
        38 --> 3 + 8 --> 11
        11 --> 1 + 1 --> 2 
    Since 2 has only one digit, return it.
    ------------------------
    Example 2:
    Input: num = 0
    Output: 0
    '''
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


def fizz_buzz(n: int) -> str:
    '''412. Fizz Buzz
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

    Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

    Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    '''
    aa = []
    for i in range(1, n+1):
        if i % 15 == 0:
            aa.append("FizzBuzz")
        elif i % 3 == 0:
            aa.append("Fizz")
        elif i % 5 == 0:
            aa.append("Buzz")
        else:
            aa.append(str(i))
    return aa


def judgeCircle(moves: str) -> bool:
    ''' 657. Robot Return to Origin

    There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
    Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

    You are given a string moves that represents the move sequence of 
    the robot where moves[i] represents its ith move.
    Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

    Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

    Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the 
    right once, 'L' will always make it move left, etc. Also, assume that the magnitude of 
    the robot's movement is the same for each move.

    Example 1:
    Input: moves = "UD"
    Output: true
    Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so 
    it ended up at the origin where it started. Therefore, we return true.

    Example 2:
    Input: moves = "LL"
    Output: false
    Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. 
    We return false because it is not at the origin at the end of its moves.'''
    x, y = 0, 0
    for i in range(0, len(moves)):
        if moves[i] == 'U':
            y += 1
        if moves[i] == 'D':
            y -= 1
        if moves[i] == 'R':
            x += 1
        if moves[i] == 'L':
            x -= 1

    if x==0 and y==0:
        return True
    else:
        return False


class PowerOf:
    def isPowerOfTwo(self, n: int) -> bool:
        '''231. Power of Two
        Given an integer n, return true if it is a power of two. Otherwise, return false.
        An integer n is a power of two, if there exists an integer x such that n == 2^x.

        Example 1:
        Input: n = 1
        Output: true
        Explanation: 2^0 = 1

        Example 2:
        Input: n = 16
        Output: true
        Explanation: 2^4 = 16

        Example 3:
        Input: n = 3
        Output: false
        '''  
        if n < 1:
            return False
        while n%2 == 0:
            n /= 2
        return True if n==1 else False

    def isPowerOfThree(self, n: int) -> bool:
        '''326. Power of Three
        Given an integer n, return true if it is a power of three. Otherwise, return false.
        An integer n is a power of three, if there exists an integer x such that n == 3^x.
        --------------------------
        Input: n = 27
        Output: true
        --------------------------
        Input: n = 0
        Output: false
        --------------------------
        Input: n = 9
        Output: true
        --------------------------
        Constraints: -2^31 <= n <= 2^31 - 1
        '''
        if n < 1:
            return False
        while(n%3 == 0):
            n /= 3
        return True if n==1 else False

    def checkPowersOfThree(self, n: int) -> bool:
        '''1780. Check if Number is a Sum of Powers of Three 
        Given an integer n, return true if it is possible to represent n as the sum of 
        distinct powers of three. Otherwise, return false.
        An integer y is a power of three if there exists an integer x such that y == 3^x.
        --------------------------
        Input: n = 12
        Output: true
        Explanation: 12 = 3^1 + 3^2
        --------------------------
        Input: n = 91
        Output: true
        Explanation: 91 = 3^0 + 3^2 + 3^4
        --------------------------
        Input: n = 21
        Output: false
        --------------------------
        '''
        while n > 1:
            n, r = n//3, n%3
            if r == 2:
                return False
        return True

    def isPowerOfFour(self, n: int) -> bool:
        '''342. Power of Four
        Given an integer n, return true if it is a power of four. Otherwise, return false.
        An integer n is a power of four, if there exists an integer x such that n == 4^x.
        ------------------------
        Input: n = 16
        Output: true
        ------------------------
        Input: n = 5
        Output: false
        ------------------------
        Input: n = 1
        Output: true
        ------------------------
        Constraints: -2^31 <= n <= 2^31 - 1
        '''
        if n < 1:
            return False
        while(n%4 == 0):
            n /= 4
        return True if n==1 else False


class rand:
    ''' 470. Implement Rand10() Using Rand7()
    :rtype: int
    Given the API rand7() that generates a uniform random integer in the range [1, 7], write 
    a function rand10() that generates a uniform random integer in the range [1, 10]. 
    You can only call the API rand7(), and you shouldn't call any other API. Please do not use 
    a language's built-in random API.

    Each test case will have one internal argument n, the number of times that your implemented 
    function rand10() will be called while testing. Note that this is not an argument passed to rand10().
    ------------------------
    Input: n = 1
    Output: [2]
    ------------------------
    Input: n = 2
    Output: [2,8]
    ------------------------
    Input: n = 3
    Output: [3,8,10]
    ------------------------
    Constraints: 1 <= n <= 10^5
    '''
    def rand10(self):
        """ :rtype: int
        reference: https://blog.csdn.net/fuxuemingzhu/article/details/81809478
        """
        return self.rand40() % 10 + 1

    def rand7(self):
        return random.randint(1, 7)

    def rand49(self):
        """
        random integer in 0 ~ 48
        """
        return 7 * (self.rand7() - 1) + self.rand7() - 1
    
    def rand40(self):
        """
        random integer in 0 ~ 40
        """
        num = self.rand49()
        while num >= 40:
            num = self.rand49()
        return num
