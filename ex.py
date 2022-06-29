def selection_sort(L):
    # for loop to go through the list, min_index and i -> index 0
    for i in range(len(L) -1):
        min_index = i
        # second for loop that compare min_index to all other items after it i + 1 -> index1, but for loop keeps moving it through the list
        for j in range(i+1, len(L)):
            # if index1 < index0
            if L[j] < L[min_index]:
                min_index = j
                # edge case, if/when item index i < item index j NO SWAPPING when min_index && i equal to the same index 
        if i != min_index:
            # otherwise... if min_index && i not equal, temp holds i 
            temp = L[i]
            L[i] = L[min_index]
            L[min_index] = temp
    return L                
selection_sort(L = [4,2,6,5,1,3])


