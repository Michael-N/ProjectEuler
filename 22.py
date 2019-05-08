'''
Author:    Michael Sherif Naguib
Date:      May 7, 2019
@:         University of Tulsa

Question #22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?




names.txt has been renamed to 22_number.txt
and here is the link to the file... https://projecteuler.net/project/resources/p022_names.txt
'''
#generate a lookup... too lazy to type out the dictionary created here...
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaLookup={}
for letter_idx in range(0,len(alpha)):
    alphaLookup[alpha[letter_idx]] = letter_idx+1 # we were told C=3 so it indexes by 1 ==> a=1 ... add 1 to account for that...     

if __name__ =="__main__":
    #reads the names from the file and creates a list of strings
    names_list = open("22_number.txt",'r').read().replace('"',"").split(",")

    #sort the list... python has native support
    sorted_names_list = sorted(names_list)

    #A function which determines score:   maps each letter in name to number c-->3 for example... then multiplys by it's position
    #   plus 1 because as the prompt indicated ' 938th' they are using ordinal numbers (which index by 1) this
    #   code assumes it will be passed an index for which in context it is indexed by 0.... the 1 corrects for this....
    nameScore = lambda name,idx: sum(list(map(lambda letter: alphaLookup[letter],name)))*(idx+1)

    #Calculate the scores: passes each name and its index through the nameScore function 
    nameScores = list(map(lambda idx: nameScore(sorted_names_list[idx],idx), list(range(0,len(sorted_names_list)))))

    #Given in the problem statement... 938th COLIN  adjust index for ordinal index by 1 to computer index by 0
    #print(sorted_names_list[937])
    #print(nameScores[937])

    #I ❤️ 🐍 oneliners
    print(sum(nameScores))






