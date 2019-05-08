'''
Author:    Michael Sherif Naguib
Date:      May 7, 2019
@:         University of Tulsa

Question #20:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

if __name__ == "__main__":

    '''
    my approach: iteration ... i think recursion might exceed pythons recursive depth and it will use a lot of memory
    '''
    #Find the factorial
    num=1
    for i in range(2,101):#note bound is exclusive.. so it is 2-100
        num = num*i

    #convert to a string
    strNum=str(num)
    #Sum
    digitSum=0
    for d in strNum:
        digitSum+= int(d)
    #print
    print(digitSum)




    