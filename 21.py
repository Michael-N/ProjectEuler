'''
Author:    Michael Sherif Naguib
Date:      May 7, 2019
@:         University of Tulsa

Question #21:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
#proper divisors of n (numbers less than n which divide evenly into n).
def properDivisors(n):
    pd=[]
    for i in range(1,n):#exclusive of n
        if n%i==0:
            pd.append(i)
    return pd

#Proper Divisor Sum of a number
def d(n):
    return sum(properDivisors(n))

if __name__ == "__main__":
    '''
        my approach: seeing in the example problem that d(n)= k where it is possible k> n  then it seams to me that there might be collisions -->
                     i.e when computing whether two numbers are amicable ... we might get some repetes....

    '''

    cache={}#Key: i Value: d(i)
    amicableNums = set()
    excclusiveMax=10000
    #Methodology: compute every one and put result numbers as the key in the cache and reverse cache...
    for a in range(1,excclusiveMax):# all nums under 10k ...( excluding 10k)
        #compute the Proper Divisor Sum
        b0 = d(a)
        #save our result: key:i value: d(i)
        cache[a]=b0
        #check if it was already computed
        b1 = None
        if b0 in cache:
            b1=cache[b0]
        else:#else it was not computed... so do it
            b1 = d(b0)
        
        #compare the results
        if b1 == a and a != b0 and a not in amicableNums:
            amicableNums.add(a)
    
    amicableNumsSum=sum(amicableNums)
    print(amicableNumsSum)


        

    
    #Compute the collisions...
