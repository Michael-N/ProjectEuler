'''
Author:    Michael Sherif Naguib
Date:      October 17, 2018
@:         University of Tulsa

Question #9: 
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc
Example:  For example, 32 + 42 = 9 + 16 = 25 = 52.
'''
def isTriplet(a,b,c):
    return pow(a,2)+pow(b,2)==pow(c,2)

def mainProgram():#in a function so the loops can be easily broken
    #brute force approach
    for c in range(0,1000):
        for b in range(0,c):
            for a in range(0,b):
                if b+a+c ==1000 and isTriplet(a,b,c):
                    msg="a:{0} b:{1} c:{2}".format(a,b,c)
                    prod=a*b*c
                    print(msg)
                    print("Prod:"+str(prod))
                    return (msg,prod) 
if __name__=="__main__":
    mainProgram()#see comment in this function

