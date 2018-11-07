'''
Author:    Michael Sherif Naguib
Date:      November 5, 2018
@:         University of Tulsa

Question #15: How many such routes are there through a 20×20 grid?
Example: Starting in the top left corner of a 2×2 grid, and only being able to move 
         to the right and down, there are exactly 6 routes to the bottom right corner.
'''
#factorial of a number N
def factorial(n):
    # n! = (n-1)! * n
    if(n==1):#base state
        return 1
    else:#degenerate... 
        return n*factorial(n-1)

#binomial coefficient (not used here for speed disadvantage...)
def binomial_coefficient(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

if __name__=="__main__":
    '''
        === BEGIN RESEARCH ===
        The number of paths is (n+k k) for an n*k shape.. (research) 
        === END RESEARCH ===
        === BEGIN REASONING ===
        so implementing this... there is a way to speed up calculation...
        = (n+k)!/(n)!*(n+k-n)! ==> (n+k)!/n!*k!
        n=k for this question
        (2n)!/((n!)*(n!))
        can save n! 
    '''
    #Settings
    X = 20

    #calculation
    n=factorial(X)
    t = factorial(2*X)
    path_count = t//(n*n)# t/(n^2) will be an integer anyway... so explicitly integer divide

    #display
    print(str(path_count))

