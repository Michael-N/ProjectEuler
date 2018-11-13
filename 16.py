'''
Author:    Michael Sherif Naguib
Date:      November 7, 2018
@:         University of Tulsa

Question #16: What is the sum of the digits of the number 2^1000?
Example:     
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

'''
if __name__=="__main__":
    #imports
    import math
    from functools import reduce

    #calculate
    p=1
    for i in range(0,1000):#multiply 2 1000 times i.e 2^1000W
        p = p*2

    #get the digits as a string
    sp = str(p)

    #iterate over the string converting each number to an integer in a list
    nums = list(map(lambda x: int(x),sp))

    #sum the list
    sum_str = str(reduce(lambda x,y: x+y, nums))

    #print
    print(sum_str)
