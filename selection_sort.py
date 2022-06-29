"""
1. initialize a variable at index 0 which will hold the value of the item in that index

     0,1,2,3,4,5    (index)
L = [4,2,6,5,1,3]

2. start for loop with i, which will be at len(of_list) - 1

3. another for loop with j, which will be i+1

"""

L = [4,2,6,5,1,3]
print(L, 'before selection sort')
def selection_sort(L):

    for i in range(len(L) -1):
        min_index = i 
        for j in range(i+1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        if i != min_index:
            temp = L[i]
            L[i] = L[min_index]
            L[min_index] = temp
    print(L)
    return L

selection_sort(L = [4,2,6,5,1,3])


"""
question for Daniel JS maybe? 
why not use enumerate?
"""