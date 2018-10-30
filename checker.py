#!/usr/bin/env python

'''
    Check sum checker for student ID of Kobe Univ.
    by Akira Kageyama, Kobe Univ.
    on 2018.10.30

    ---

    A student num is 7 digits, e.g., 1234567
    Third from the left (3 above) is the check digit.

    Let
        checksum = ( 4*1+5*2+6*4+7*5+8*6+9*7 ) % 11
    where
           checksum = {0, 1, 2, ..., 8, 9, 10}
        check digit = {1, 1, 2, ..., 8, 9, 0}
    check digit is given by
        select case (checksum)
          case 10:
            check digit = 0
          case 0:
            check digit = 1
          default:
            check digit = checksum

    --------
     or in short,
                       checksum = { 0, 1, 2, ..., 8, 9, 10}
                (10+9*checksum) = {10,19,28, ...,82,91,100}
     Their 2nd digit from right    |  |  |       |  |   |
                (10+9*checksum) = {1, 1, 2,  ...,8, 9,  0 }
     These are the check digits.
'''

class Digits:
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i7 = 0
    i7 = 0

    def separate_digits(self, num):
        self.i7 = num % 10
        num = (num - self.i7) // 10
        self.i6 = num % 10
        num = (num - self.i6) // 10
        self.i5 = num % 10
        num = (num - self.i5) // 10
        self.i4 = num % 10
        num = (num - self.i4) // 10
        self.i3 = num % 10
        num = (num - self.i3) // 10
        self.i2 = num % 10
        num = (num - self.i2) // 10
        self.i1 = num % 10

    def check(self, num):
        self.separate_digits(num)
        sum = self.i1 * 4 \
            + self.i2 * 5 \
            + self.i4 * 6 \
            + self.i5 * 7 \
            + self.i6 * 8 \
            + self.i7 * 9
        mod11 = sum % 11
        # if mod11==0:
        #     ans = 1
        # elif mod11==10:
        #     ans = 0
        # else:
        #     ans = mod11
        # or in a one-liner...
        ans = ( (10+9*mod11) // 10) % 10  # 2nd digit from right
        if self.i3 == ans:
            print('Correct.')
        else:
            print('Incorrect!')


if(__name__ == "__main__"):
    digits = Digits()

    num = int(input("Enter num: "))
    digits.check(num)
