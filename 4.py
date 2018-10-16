'''
Author:    Michael Sherif Naguib
Date:      October 2, 2018
@:         University of Tulsa

Question 4#: 

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''


def isPallindromicNumber(num):
    strNum= str(num)
    return strNum==strNum[::-1]

if __name__=="__main__":
    largest=0
    for i in range(99,999):
        for j in range(99,999):
            prod=i*j
            #schort circuit eval first
            if(prod>largest and isPallindromicNumber(prod)):
                largest=prod        
    print(largest)
