'''
Author:    Michael Sherif Naguib
Date:      Occtober 10, 2018
@:         University of Tulsa

Question 7#: What is the 10 001st prime number?
Example: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.    
'''
isPrime=__import__("3").isPrime
import math

#Making this code a function so that it can be used in 10.py
#UPDATE: October 23 2018 I just realied I dont necessarily need to find the primes 1-n
#        but exclude but exclude all non primes in a list 1-n which is similar
#        but can be implemented faster... this is done in 10.py
def findPrimesUpto(N):
    
    count=1#The number of primes fount so far
    primes=[2]#an array storing the primes found
    i=3#initial number to check for primality

    while count<N:#calculations:
        didEvenlyDivide=False
        sqrtOfPotentialPrime = math.sqrt(i)#outside the loop to be more efficient
        
        #for every prime already found
        for j in range(1,len(primes)):#start at index one because the iteration skips all numbers powers of 2
            
            #Does it divide?
            p = primes[j]#cache the value
            if i/p== i//p:#integer division... check if the same...
                didEvenlyDivide=True
                break

            #if none of the factors below that number did not work then the sqrt is the max
            #there could exist a factor
            if p>sqrtOfPotentialPrime:
                break
        #Append To the list of primes
        if(not didEvenlyDivide):
            primes.append(i)
            count+=1
        i+=2#skip 2
    return primes

if __name__=="__main__":
    #setup
    N=10001
    primes = findPrimesUpto(N)
    #print
    print(primes[len(primes)-1])