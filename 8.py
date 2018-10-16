'''
Author:    Michael Sherif Naguib
Date:      October 16, 2018
@:         University of Tulsa

Question #8: Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
Example:    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832. 

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

#checks if the item has the string hasThis
def contains(item,hasThis):
    return hasThis in item

#product of numbers in a list
def prod(listOfValues):
    prod=1
    for item in listOfValues:
        prod*=item
    return prod

#Main
if __name__=="__main__":
    #read the number
    eight_number=open("8_number.txt",'r')
    n = eight_number.readline()
    
    #setup
    intervalWithHighestProd=[0,13]
    highestProd=0

    #iterate over the number as a string
    currentIndex=0
    lenN = len(n)
    while(currentIndex<lenN-13):

        #get the current string
        currentSection=n[currentIndex:currentIndex+13]
        #print(str(currentSection),"")
        if not contains(currentSection,"0"):
            # if there is a 0 this means that you can break... a more efficient program might find the index
            # of that zero and then skip till that zero is out of the currentSection
            #split number into digit list
            splitNumberStrs = list(currentSection)
            #convert to integers
            splitNumbers = map(int,splitNumberStrs)
            #find the product
            currentProd=prod(splitNumbers)
            #update

            if(currentProd>highestProd):
                highestProd = currentProd
                #print("current Prod"+str(currentProd))
                intervalWithHighestProd = [currentIndex,currentIndex+13]
        #else:
            #print("Zero")
        currentIndex+=1

    #print(n[intervalWithHighestProd[0]:intervalWithHighestProd[1]]) 
    print(highestProd)         
            

