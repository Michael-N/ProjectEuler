'''
Author:    Michael Sherif Naguib
Date:      October 31, 2018
@:         University of Tulsa

Question #11: 

    What is the greatest product of four adjacent 
    numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


Example: (below)

In the 20×20 grid below, four numbers along a diagonal line have been marked in red. (put in ||)

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 |26| 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 |63| 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 |78| 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 |14| 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

'''
#takes a space seperated  newline seperated row text file of numbers and turns it into a 2d array
def parse_file_grid(filename):
    #legit one of the coolest lines of code i think i have written... ( technically i wrote it out then converted it to a 1 liner)
    #but it is still cool ... readability = readibility- number of lines lost :/
    return list(map(lambda row:list( map(int,row)), list(map(lambda ln: ln.split(" "),open(filename,"r").readlines()))))

#retruns the product of a list
def prod_list(l):
    p=1
    for num in l:
        p = p*num
    return p

#main program
if __name__=="__main__":
    length_of_sequence=4
    #read the grid from the file
    grid = parse_file_grid("11_number.txt")
    #print(grid)

    #current largest corresponding Product:
    p_max = 0

    #iterate
    l = len(grid)#asuming grid is square
    for i in range(0,l-length_of_sequence+1):#ensure not out of bounds for the iteratin
        for j in range(0,l-length_of_sequence+1):
            #print(str(i)+" "+ str(j))
            #check the cases..
            '''
                horizontal a,b sequences ,diagonal sequences,vertical a,b sequences
                    _____
                    | \/ | b
                    | /\ |
                 a  -----
            '''
            all_cases=[]
            #horizontals                        ______________                                | 
            all_cases = all_cases+ [grid[i][j:j+length_of_sequence],grid[i+length_of_sequence-1][j:j+length_of_sequence]]
            #diagonal
            diagonal_sequence_a = []
            diagonal_sequence_b = []
            for k in range(0,length_of_sequence):
                diagonal_sequence_a.append(grid[i+k][j+k])#NOTE to self: corrected a mistake here grid[i+k][j+k] not grid[i+k][i+k] 
                diagonal_sequence_b.append(grid[i+k][j+length_of_sequence-1-k]) #use j as the cordinate for the iteration
            all_cases = all_cases+ [diagonal_sequence_a,diagonal_sequence_b]
            #vertical
            vertical_sequence_a=[]
            vertical_sequence_b=[]
            for m in range(0,length_of_sequence):
                vertical_sequence_a.append(grid[i+m][j])
                vertical_sequence_b.append(grid[i+m][j+length_of_sequence-1])
            all_cases = all_cases+ [vertical_sequence_a,vertical_sequence_b]

            #calculate the products
            prods = list(map(prod_list,all_cases))
            #print(str(all_cases))
            #find the index of the max
            item_index = prods.index(max(prods))
            #reassign the max for the grid if greater
            if prods[item_index]>p_max:
                p_max = prods[item_index]
    print(str(p_max))


