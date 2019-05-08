'''
Author:    Michael Sherif Naguib
Date:      May 8, 2019
@:         University of Tulsa

Question #24:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the 
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

if __name__ == "__main__":
    '''
    create permutation generator
    sort
    '''

    #excludes 10 so it is 0-9 ==> string digits 0-9 
    strDigits = set(map(lambda d: str(d),list(range(0,10))))

    #creates permutations of all (must be string) items in a set  
    def recursivePerms(itemsSet):
        allPerms=set()#holds all permutations
        for item in itemsSet:#grab one all the differnt items for the first
            #get the sub permutation grabbing all items that are not the item we grabbed first ...
            #   this is a recursive call so it travels down until there is only one item left to add
            subPerms = recursivePerms(itemsSet.difference(set(item))) 

            #if there are multiple items then we still have to add the permutation to the sub permutation (recombine)
            if len(subPerms)>0:
                for subItem in subPerms:
                    allPerms.add(item+""+subItem)
            else:#we hit our  base case ( subPerms ran out of items to recombine recursivly so we pass the one item we have...)
                return set(item)
        return allPerms

    #Run the calculation.... 
    #    this takes the digits finds the permutations then converts the strings to integers then finally sorts the integer list
    sortedPermutations = sorted(list(map(lambda x: int(x),list(recursivePerms(strDigits)))))

    #get the millionth item ( note the list was indexed by 0 so the millionth item is at 1mil -1)
    print(sortedPermutations[999999])
    