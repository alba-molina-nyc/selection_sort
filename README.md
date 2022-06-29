# Selection Sort

- for selection sort you are going to need the indexes of the list
- you need to keep track of the index with the lowest value so far by initializing a variable (min_index) to hold it
  - min_index initialized by first for loop (at index0)
- you need to start a for loop to keep track of the number at index1 (the j for loop)
- compare min_index with j
- if j < min_index, min_index now holds j
  - work your way all the way to end of the list and min_index will keep the lowest value
  - once at the end of the list, you have the smallest value in min_index, you swap it with i

### RINSE AND REPEAT

# Steps

- for selection sort you are going to need the indexes of the list
- you need to keep track of the index with the lowest value so far by initializing a variable (min_index) to hold it
  - min_index initialized by first for loop (at index0)
- you need to start a for loop to keep track of the number at index1 (the j for loop)
- compare min_index with j
- if j < min_index, min_index now holds j
  - work your way all the way to end of the list and min_index will keep the lowest value
  - once at the end of the list, you have the smallest value in min_index, you swap it with i

# EX

1. (i) will be the 4 at index0
2. save min_index to i
3. (j) next for loop i + 1 sets j at 2, index1
   i,j
   L = [4,2,6,5,1,3]
   ind=[0,1,2,3,4,5] (indexes)

go through the whole list & compare min_index with j
if item in list < min_index, switch until you reach the end of the list

i.e.)

        L = [4,2,6,5,1,3]
        min_index=0
        min_index=1
        min_index=4

then you switch item at index 4, with the item at index 0 because that is where you started, so you end up with:

        L = [1,2,6,5,4,3]

RINSE AND REPEAT
now you move i,j min index set to i and i is is set to index1
min_index=1
No switch because 2 is the next smallest

now you move i,j min index set to i and i is is set to index2
min_index=2
j = i + 1 aka index3

compare min_index with j until go through list

                 i,j
        L = [1,2,6,5,4,3]
        min_index = 2
        min_index = 3
        min_index = 5

then you switch item at index5, with the item at index 2 because that is where you started, so you end up with:

        L = [1,2,3,5,4,6]
        RINSE AND REPEAT UNTIL THE WHOLE LIST IS SORTED
