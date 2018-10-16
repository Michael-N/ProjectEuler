'''
Author:    Michael Sherif Naguib
Date:      October 10, 2018
@:         University of Tulsa

Question 5#: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Example:2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.


'''
three = __import__("3")
isPrime=three.isPrime

#returns a list of factors including repetes ex--> [(2,6),(5,2)] --> 2^6 * 5^2
def factors(n):
    #is based off the factorAndReduce function in question #3
    for i in range(2,n+1):# include n it may be prime?
        if n%i==0 and isPrime(i):
            c=0#it will always reduce at least once... so c is incremnted
            while(n%i==0):# reduce as much as possible
                c+=1
                n/=i
            return [(i,c)] + factors(int(n))# add that number to the list then return the recursion
    return [(n,1)] #otherwise n is prime

if __name__=="__main__":
    #evenly divisible from 1 to N
    N=20

    #find the factors for the numbers 1-20
    factorsList=[]
    for i in range(N,0,-1):
        factorsList+=factors(i)
    #print(factorsList)

    #Get all the unique factors
    uniqueFactors=[]
    for i in range(0,len(factorsList)):
        if factorsList[i][0] not in uniqueFactors:
            uniqueFactors.append(factorsList[i][0])
    #print(uniqueFactors)

    #Get the highest exponent for each factor:
    highestExponent=[1]*int(len(uniqueFactors))
    for i in range(0,len(uniqueFactors)):
        for item in factorsList:
            if uniqueFactors[i]==item[0] and highestExponent[i]<item[1]:
                highestExponent[i]= item[1]
    #print(highestExponent)
    #print(uniqueFactors)

    #now each unique factor in uniqueFactors has its associated highest expontent 
    #in the same index in the list highestExponent
    #the result is the product of all the factors raised to their associated exponent
    numResult=1
    for i in range(0,len(uniqueFactors)):
        numResult*=pow(uniqueFactors[i],highestExponent[i])
    print(str(numResult))

