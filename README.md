# Selection Sort

- for selection sort you are going to need the indexes of the list
- you need to keep track of the index with the lowest value so far by initializing a variable (min_index) to hold it
  - min_index initialized by first for loop (at index0)
- you need to start a for loop to keep track of the number at index1 (the j for loop)
- compare min_index with j
- if j < min_index, min_index now holds j
  - work your way all the way to end of the list and min_index will keep the lowest value
  - once at the end of the list, you have the smallest value in min_index, you swap it with i

### Steps

1. initialize a variable at index 0 which will hold the value of the item in that index
