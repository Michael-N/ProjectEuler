'''
Author:    Michael Sherif Naguib
Date:      July 12, 2019
@:         University of Tulsa

Question #25:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

#import the binet code i wrote in Question 2 (binets formula)
two = __import__("2")

def digit_count(n):
    #counts how many digits in the number
    return len(str(n))
      
if __name__ == "__main__":
    '''
    my approach ... use f(n) = binets formula ... figure out how to limit the search space
    
    ... I thought of implementing a sort of binary search that could eliminate any ineefficiency in finding digit counts but
    there is an easier way... 

    mathematical way: let f(n) = binets formula for nth fibonacci number       
    
    let f(n) = 10^1000 (this number has 1001 digits) ==> solve a numerical value for n round up and this is the max bound on n
    let f(n) 10^998 (this number has 999 digits) ==> solve a numberical value for n round down and this is the min bound on n

    
    Steps:
    (1) establish a reasonable max and bound:  here i increase the max bound search by a factor of 2 each time
                                                   then once i have found that the digit count for that max index is 
                                                   greater than the desired i set that as the max 
    (2) then calculate the digit count for all the numbers less than that... it is psudo efficient



    =============================================================
    New approach .... is brute force really that bad ? 

    possible issues: loss of precision using binet's formula
    '''
    #A constant to hold the max digit count
    DIGIT_COUNT = 1000
    '''
    #Keep track of the index .. (note Binet formula F(1)=F(2)=1 so the indicies are not off by 1...)
    index=1
    #Infinate loop
    while True:
        print(index)
        #Be careful when getting the length here ... two.binet for large values of index may loose precision or explode (to use a non technical term)
        l = digit_count(two.binet(index))
        #If we hit our desired property break the loop
        if l == DIGIT_COUNT:
            break
        #Otherwise increment the index and try again
        index+=1
    #The program only terminates when we get a result
    print(index)
    '''

    #iterative approach
    prev1=1#F(1)
    prev2=1#F(2)
    nextNum=None
    index=3#thus we are on index 3...
    while True:
        #Calculate the next number in the sequence
        nextNum = prev2 + prev1
        prev1 = prev2
        prev2 = nextNum
        
        #Check if it meets the condition
        l = digit_count(prev2)
        if l >= DIGIT_COUNT: 
            # it might be that the nth term jumps from n digits to n+2 or more digits ... so
            # use >= not just ==
            break
        #Increment the index: 
        index+=1 
    print(index)
    


