'''
Author:    Michael Sherif Naguib
Date:      November 5, 2018
@:         University of Tulsa

Question #14: Which starting number, under one million, produces the longest chain?
Example:     
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import math

#the collatz function
def collatz(x):
    if x//2 == x/2:
        return x/2
    else:
        return 3*x+1

#collatz sequence length n>1
def sequenceLengthCollatz(n,use_found_lengths=[]):
    length=1
    c=n
    while c!=1:
        #calculate the collatz
        c = collatz(c)
        #check already found lengths to exit early
        for num_and_len in use_found_lengths:
            if c==num_and_len[0]:
                length = length + num_and_len[1]
                return length
            if c <num_and_len[0]:#they are stored in ascending value... no use looking to see if c==n
                break
        length = length +1
    return length


if __name__=="__main__":
    '''
    it turns out it is faster just to brute force this than memorize values... however do exclude powers of 2
    '''

    MAX=1000000
    #Store which one is the largest... 
    longest_seq_len=0
    coresponding_num=0
    #2^n+1 will always have a longer length than 2^n
    n=math.floor(math.log(float(MAX),2))# puts 2^n=c for c is closest but below max 2^n  n+1 length 
    #a list of (number,collatz length) 
    found_num_len_pairs = []#[(int(math.pow(2,p)),p+1) for p in range(0,n)] #it would now appear that 'memorizing' jumps is not faster 
    #print(found_num_len_pairs)
    #print(str(found_num_len_pairs))

    #iterate to calculte
    for i in [x for x in range(1,MAX) if math.log(x,2)!=int(math.log(x,2))]:#ignore powers of 2
        #calculate the sequence
        s = sequenceLengthCollatz(i,found_num_len_pairs)
        if i//1000 == i/1000:
            print("Longest Sequence= {} Current Seed Num={} Sequence Len={} mem={}".format(longest_seq_len,i,s,len(found_num_len_pairs)))
            #print(str(found_num_len_pairs))
        #append a new found sequence length
        #found_num_len_pairs.append((i,s))  .... found that this actually slows it down signifigantly!! it is much faster only
        #                                        to check if it is a power of 2 then use that value to skip
        #if it is the longest sequence
        if s>longest_seq_len:
            longest_seq_len=s
            coresponding_num = i
    print(str(coresponding_num)) 
        
