'''
Author:    Michael Sherif Naguib
Date:      November 14, 2018
@:         University of Tulsa

Question #17: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
Example:    
(NOTE exclude hyphens) 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
'''
import math
#looks up n in a list data of tupels where item[0] is compared with n and item[1] returned if true
def lookup(n,data):
    for item in data:
        if(item[0]==n):
            if len(item[1])!=0:
                # print(item[1]+ "   " + str(len(item[1])))
                print(item[1],end=' ')
            return item[1]

#gets the Nth digit of a number INDEX by 0...  i.e num=54321   n=0   returns 5
def getNthDigit(num,n):
    strN = str(num)
    return int(strN[n])

#count the number of n: 45--> forty five INCLUDES 'and' ex. 154--> one hundred and fifty four
def count(n,parsing_data):
    strN = str(n)
    strL = len(strN)
    current_count=0
    #iterate over the number...skipping the last digit since it has to be handled by the 1
    for place in range(0,strL):
        #Edge Case: (1)digit number 
        if strL==1:  
            current_count = current_count+ len(lookup(n,parsing_data))
            return current_count
        
        #Edge case: handle 2nd digit place
        if place == strL-2:
            digit = getNthDigit(n,strL-2)#get the digit for the num 34 --> 3
            #(10-19) if  digit <20 
            if digit<2:#lookup
                current_count = current_count+ len(lookup(int(strN[strL-2:strL]),parsing_data))
                return current_count
            #(20-90) else the digit is 20-90:  num=24 -- > lookup 2*10 +    (count or lookup) 4
            else:
                last_digit = int(strN[strL-1:strL])
                current_count = current_count+ len(lookup(digit*10,parsing_data)) + count(last_digit,parsing_data)
                return current_count
        
        #any other digits.. skip the last digit place because it is handled by recursion and the edge case... 
        if place != strL-1:
            if (place <= strL-3) and (int(strN[place+1:strL])!=0):#check if it is 100> and if the tail is not all 0's
                # third to last digit... ie. the number needs an 'and'... but the number only needs if the last digits are not all 0
                #100 is not one hundred and just one hundred... nore 500.... etc...
                current_count=current_count+3#THIS IS FOR THE 'and' 545 = five hundred and forty five ==> 
            front_digit = getNthDigit(n,place)
            if(front_digit == 0):#if the digit is zero ex  34045 just continue with the next place in the loop
                continue
            else: 
                exponent = (strL-place-1)# consider 5000  = 5*10^3   indexed 0,1,2,3 when len 4 the exponent is as written
                current_count = current_count+ count(front_digit,parsing_data) + len(lookup(math.pow(10,exponent),parsing_data))# ex 5324 ==> five + thousand --> lookup 5 + lookup 1000 ... the loop will handle the other digits
    return current_count       


if __name__=="__main__":
    #Hey can you do this..... in a one liner? challenge accepted
    #from functools import reduce
    #l=[[1,2,3],[4,5,6],[7,8,9]]
    #p=4#the number of spaces to print in... 
    #c= "_"#the empty character to print with ... note these can be specified as constants in the one liner...
    #print( "".join(list(reduce(lambda str_row,n_lst: str_row+["\n"]+n_lst ,list(map(lambda row: list(map(lambda item:(str(item)+(p*c))[0:p],row)),l))))))

    #parsing data: yes just the length of the string could be programed but this imporves readibility
    #having the values in this way might be more benificial if were asked to figure out for any arbritrary number...
    pd = [(0,''),(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five"),(6,"six"),(7,"seven"),(8,"eight"),(9,"nine")]
    pd = pd +[(10,"ten"),(11,"eleven"),(12,"twelve"),(13,"thirteen"),(14,"fourteen"),(15,"fifteen")]
    pd = pd + [(16,"sixteen"),(17,"seventeen"),(18,"eighteen"),(19,"nineteen")]#Hours lost here: 5+ ... mispelled nineteen as ninteen
    pd = pd + [(20,"twenty"),(30,"thirty"),(40,"forty"),(50,"fifty"),(60,"sixty"),(70,"seventy"),(80,"eighty"),(90,"ninety")]
    pd = pd + [(100,"hundred"),(1000,"thousand")]
    #could be expanded pd = pd + [(1000000,"million")]

    total_count=0
    for i in range(1,1001):# 1 to 1000 inclusive
        print("calc i="+str(i))
        current = count(i,pd)
        print("\n>>>  i:"+str(current))
        total_count= total_count + current

    print(str(total_count))

                

