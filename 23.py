'''
Author:    Michael Sherif Naguib
Date:      May 7, 2019
@:         University of Tulsa

Question #23:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 

For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum 
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written 
as the sum of two abundant numbers. 

However, this upper limit cannot be reduced any further by analysis even though it is known 
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

#recall a proper divisors function was written in problem #21 
twentyOne = __import__("21")
properDivisorSum = twentyOne.d#was called d in that problem statement... NOTE! i will refer to this by d(n)

'''
    By the problem statement we are told our min is 24 and the max 28123 ...so find all the abundant numbers 
    we know that limit or 'critical num' is less than 28123 but we dont know if it is one less or a thousand less

   Thus find d(i) for i ∈ [13,28123) and determine which are abundant an which are not
'''

#Determines if a number is an abundant number...
def isAbundant(n):
    result = properDivisorSum(n)
    return result>n

if __name__=="__main__":
    #the number for which past this it is know all numbers can be represented as the sum of two abundant nums....
    KNOWN_LIMIT=28123

    #Create a list of all the abundant numbers in our desired range... NOTE! this is the slowest part of the calculation and would benifit from distribution!
    abundantNumbers=[]
    for i in range(12,KNOWN_LIMIT):
        if isAbundant(i):
            abundantNumbers.append(i)

    '''
       Iterate twice over the list:  
           strategy iterate from the left adding to the right ... 
           when the right and the left hit a sum > max we pass up *** some iterations***

           This relies on the fact that the list we will obtain is in ascending order.... 
           abundant numbers were found and appended in increasing order so the list is sorted!
    
            if we reach a situation where holding the right iterator index constant and we iterate the 
            left values and since it is sorted if one of these values hits a sum greater than our max we can skip the remaining on
            the left iterator as we know the sum will only increase

       our range is [1,28123] for which numbers are abundant and which are not
    '''

    #Will store any number which is the sum of two non abundant numbers (using set for benifit lookup speed and we dont need order)
    removeFromRange=set()
    #our iteration variables
    i=0
    j=len(abundantNumbers)-1

    #while the left iterates hold the right 'constant' then decrement the right...   not necessarily N^2 ... dependant on distribution and frequency of abundant numbers....
    while j >= 0:#RIGHT ITERATION
        while i < len(abundantNumbers):#LEFT ITERATION
            sumVal = abundantNumbers[i] + abundantNumbers[j]
            if sumVal >= KNOWN_LIMIT:
                break# Breaks the left iteration loop
            else:
                removeFromRange.add(sumVal)
            i+=1#increment
        i=0#reset for next iteration...
        j-=1#Decrement
    
    #print(str(list(removeFromRange)))
    #for sum reason ;) i got the sum of 1 to KNOWN_LIMIT ... found i forgot to add my numbers to remove range list ('else' statement ln 77)

    #Now create a set of all the numbers in our range 
    allNums = set(range(1,KNOWN_LIMIT))

    #Now find the difference: these are the numbers which cannot be expressed as the sum of two non abundant numbers
    remainingNums = allNums.difference(removeFromRange)

    #now find the sum
    print(sum(remainingNums))
