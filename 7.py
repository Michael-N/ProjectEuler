'''
Author:    Michael Sherif Naguib
Date:      Occtober 10, 2018
@:         University of Tulsa

Question 7#: What is the 10 001st prime number?
Example: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.    
'''
isPrime=__import__("3").isPrime
if __name__=="__main__":
    #setup
    N=10001
    count=1
    i=2
    primes=[2]

    #calculations: sieve of eratosthenes
    while count<N:
        didEvenlyDivide=False
        for j in range(0,len(primes)):
            if i%primes[j] == 0:
                didEvenlyDivide=True
                break
        if(not didEvenlyDivide):
            primes.append(i)
            #print(i)
            count+=1
        i+=1
    
    #print
    print(primes[len(primes)-1])