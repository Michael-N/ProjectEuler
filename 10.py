'''
Author:    Michael Sherif Naguib
Date:      October 23, 2018
@:         University of Tulsa

Question #10:Find the sum of all the primes below two million.
Example:  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.    
'''
import math

def sumList(numList):
    sum=0
    for item in numList:
        sum = sum + item
    return sum


def sieveOfEratosthenesFailedAttempt(N):
    reducedPrimes = list(range(2,N))
    i=0
    while(i<len(reducedPrimes)):#recalculate the length of the array ...this is slow... keep track of how many are removdedremoved
        #current item in the prime array
        cp = reducedPrimes[i]
        
        #new reduced
        newReducedPrimes = []
        for j in range(i+1,len(reducedPrimes)):#exclude the current prime and go upto the ones not checked yet...
            currentNum = reducedPrimes[j]#the current number being divided by the current prime cp
            if not (currentNum//cp == currentNum/cp):#integer division faster than modulo
                newReducedPrimes.append(currentNum)#if it does not evenly divide keep it in the list
        reducedPrimes = reducedPrimes[0:i+1] + newReducedPrimes#add the previous prime in at the font

        #increment 
        i = i+1

        #if i//100 == i/100:
        #    print("Reduced Len ["+str(len(reducedPrimes)) + "] Removing numbers Divisible by Prime [" + str(cp)+"] ["+ str(i)+" items done]")
    return reducedPrimes

def sieveOfEratosthenes(N):
    currentNumbers = [2]+list(range(3,N,2))#excludes all numbers that are multiples of 2 then 2 put at front of the list...
    i=0
    n_root = math.ceil(math.sqrt(N))
    while(i<len(currentNumbers) and i<n_root):
        j=1
        p = currentNumbers[i]#the current prime
        #print("removing for prime="+str(p))
        while(i+j<len(currentNumbers)):#exclude the prime at i therefore j is 1 initially not 0
            currentNum = currentNumbers[i+j]    
            if currentNum//p == currentNum/p:#test if divides ..if so delete
                #print("        deleting num="+str(currentNum))
                del currentNumbers[i+j]#delete that number... do NOT increment j as the next number is now at the same index
            else:
                #the number was not deleted move onto the next...
                j = j+1
        i = i+1
    return currentNumbers

#made while working on 12.py in case a list of primes from a file is needed...
def savePrimes(N,fileName):
    f = open(filename,"w+")
    primes_str = reduce(lambda x,y: y + str(x), sieveOfEratosthenes(N))
    f.write(primes_str)
    f.close()


if __name__=="__main__":
    '''
        this algorithim is fast but not quite fast enough to meet 1minute... it took 10min
        that might be because of pythons time yet nontheless it was removing 2 and 
        3 that took the longest... if the list could have some base primes removed it instantly
        becomes faster by a greater degree than how it slows with N
    '''
    results = sieveOfEratosthenes(2000000)
    print(str(sumList(results)))
