'''
Author:    Michael Sherif Naguib
Date:      November 20, 2018
@:         University of Tulsa

Question #18: 
Maximum path sum I
Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)

Example:    

by starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
'''
import sys

#finds the avg over all all items in a 2D array
def findAvg2D(a_list):
    all_nums = reduce(lambda row,all_nums: all_nums+row,a_list )
    return reduce(lambda x,sum: x+sum, all_nums)/len(all_nums)

def normalize(a_list):
    l = math.sqrt(reduce(lambda x,y: x*x+y,a_list))
    return list(map(lambda x: x/l,a_list))

#makes a (deep) copy of an array
def deepCopyTwoD(twoDarray):
    copy_array=[]
    current_row=[]
    for i in range(0,len(twoDarray)):
        for j in range(0,len(twoDarray[i])):
            current_row.append(twoDarray[i][j])
        copy_array.append(current_row)
        current_row=[]
    return copy_array

#get the max of a 1D array... returns -1 if error
def getMaxIndex(oneDarray,exclude_indicies):
    max = -sys.maxsize-1
    indx=-1
    for i in range(0,len(oneDarray)):
        test_val = oneDarray[i]
        #test value anyway... bc the seccond condition is a loop check... short circuit eval might
        #                     prevent a long check if the item is not even the max when exclude list is
        #                     large
        if (test_val>max) and (i not in exclude_indicies):
            max = test_val
            indx= i
    return indx

#find decending value index --> [3,1,5] ==> [2,0,1] (indicies with highest values first)
def findValueDecendingIndicies(oneDarray):
    orderDecendingIndicies=[]
    for indx in range(0,len(oneDarray)):
        x = getMaxIndex(oneDarray,exclude_indicies=orderDecendingIndicies)
        orderDecendingIndicies.append(x)
    return orderDecendingIndicies

#get a list of Decending array values 1d example... 
def findValueDecendingIndiciesTwoD(twoDarray):
    orderDecendingIndicies=[]
    for row in twoDarray:
        #the one dimensional version...
        orderDecendingIndicies.append(findValueDecendingIndicies(row))
    return orderDecendingIndicies
            

if __name__=="__main__":
    from functools import reduce
    #read the pyramid from a file... returns a nested array where the tip of the pyramid is at index 0... 
    pyramid=list(map(lambda row: list(map(lambda num_str: int(num_str),row.split(" "))),open("18_number.txt","r").readlines()))

    
    '''My Algorithm
    _____________________
    1.) set a value s= 2D array Avg
    2.) subtract s from every item in a copy of the 2D array
    3.) look for paths... from the bottom up memorizing how in each iteration how many are above the avg or below the avg... 
        ... ?

       My Algorithm 2.0
    ________________________
    1.) store in a seperate array the indicies of the numbers in each row arranged by their corresponding number in decreasing order
        ... place indicies with higher values first in the list...
    3.) use that indicies list to assign number priority taking the number from the 
    2.) starting from the bottom pick rows iterate through the indicies list and check if the number is a valid path (check that array len)
    3.) if it is then continue to the next and select .... till the end is reached...

    '''
    #for indx in reversed(range(0,len(indexData[rowIndex]))):#start(ed) from the bottom 
    #picks an item from each row starting from the bottom iterating upwards recursivly .....
    def selectItem(twoDarray,indexData,rowIndex,prevItemIndex,chain=[]):
        
            '''
            since the length of the next row in the data i always 1 less in length than the row below it...
            therfore valid selection indicies as a binary decision are 
            the current row M  index F as context: valid choices for M+1(row above)

                  m+1   * * * * *         0 1 2 3 4
                  m    * * * * * *       0 1 2 3 4 5    as F

                  valid choices are  F-1 if F-1>0 and f if F<len(m+1)
            
            '''
            if not prevItemIndex-1 <0:
                

        #now we are here

    