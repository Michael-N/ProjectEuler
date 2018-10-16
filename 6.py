'''
Author:    Michael Sherif Naguib
Date:      October 10, 2018
@:         University of Tulsa

Question 6#: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
Example:     
'''

if __name__=="__main__":
    N=100
    
    #The sum of the numbers squared and the sum of the numbers
    sumNumSquared=0#    (a^2 + b^2)
    sumOfNum=N*(N+1)/2#         a+b
    for i in range(1,N+1):
        sumNumSquared+=i*i
    
    #sum of the numbers   squared
    sumOfNumSquared=sumOfNum*sumOfNum# (a+b)^2

    #print the result
    print(str(int(sumOfNumSquared-sumNumSquared)))