'''
Author:    Michael Sherif Naguib
Date:      October 2, 2018
@:         University of Tulsa

Question 3#: What is the largest prime factor of the number 600851475143 ?
Example:     The prime factors of 13195 are 5, 7, 13 and 29.

'''
import time
num=600851475143#   600,851,475,143


def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def factorAndReduce(n):
    for i in range(2,n+1):# include n it may be prime?
        if n%i==0 and isPrime(i):
            while(n%i==0):# reduce as much as possible
                n/=i
            return [i] + factorAndReduce(int(n))# add that number to the list then return the recursion
    return [n] #otherwise n is prime

def findLargestPrimeFactor(num):
    factors = sorted(factorAndReduce(num))#get all the factors
    print("Largest Factor is {0}".format(str(factors[len(factors)-1])))# Take the highest number=last item of list


findLargestPrimeFactor(num)

