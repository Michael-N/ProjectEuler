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

if __name__=="__main__":

    from functools import reduce

    #read the pyramid from a file... returns a nested array where the tip of the pyramid is at index 0... 
    pyramid=list(map(lambda row: list(map(lambda num_str: [int(num_str),None],row.split(" "))),open("18_number.txt","r").readlines()))
    '''

    NOTE! the pyramid is represented as a jagged tripple array: here is the form of the data...

    pyramid=[
        [ITEM]
        [ITEM,ITEM]
        [ITEM,ITEM,ITEM]
        ...
        [ITEM,ITEM,ITEM,...,ITEM]
    ]
    where each ITEM=[NUMBER,MAX_ANCESTOR_SUM]

    ex.. here the pyramid is inverted...

    [[88, False], [02, False], [77, False], [73, False], [07, False], [63, False], [67, False]]    (TOP LEVEL)
    [[19, False], [01, False], [23, False], [75, False], [03, False], [34, False]]
    [[20, False], [04, False], [82, False], [47, False], [65, False]]
    [[18, False], [35, False], [87, False], [10, False]]
    [[17, False], [47, False], [82, False]]
    [[95, False], [64, False]]
    [[75, False]]                                                                                   (BOTTOM LEVEL)

    note it decreases by one element each time... my new dynamic programming approach is to
    look at an element... if it is in the top level of the pyramid (assuming it is inverted as like above) 
    then the max_sum value (depicted as FALSE ---> will be changed to None in code revision) should be the 
    current item value, and otherwise should pick the greatest ancestor sum and add itself

    PSUDOCODE:
        iterate through each level
            if first (top) level then path sum for each element is its own number value
            otherwise on all other levels take the max of the two adjacent elements in the previous level and add that
            to the current element path sum

    example:

    [[17, 17], [47, 47], [82, 82]]   #top level so init path sum to element value
    [[95, 142], [64, 146]] # 47>17 so do 95+47=142 for the first   and    82>47 so do 64+82=146
    [[75, False]]# 146> 124 so do 146 + 75 = 221 and since this is the last level (bottom) we are done       

    
    '''
    
    
    #Note a dynamic programming strategy is used but it is just easier to keep track of that info with the item
    # [number,bestSum] ..... note could do [number,bestSum,ancestor] to determine the path...
    for level in reversed(range(0,len(pyramid))):
        #First level so best possible sum is that item...
        if level== len(pyramid)-1:
            for idx in range(0,len(pyramid[level])):
                pyramid[level][idx][1] = pyramid[level][idx][0]
        else:#otherwise for each item place the max of the previous two items.... above it
            for idx in range(0,len(pyramid[level])):#assuming pyramid shrinks by one element each time...
                #max of the two levels above
                max_ancestor_sum = max(pyramid[level+1][idx][1], pyramid[level+1][idx+1][1])
                pyramid[level][idx][1] = max_ancestor_sum + pyramid[level][idx][0]
    #the now max sum of the entire pyramid is now at the tip of the pyramid ...
    max_path_sum=pyramid[0][0][1]
    print(max_path_sum)


    


    