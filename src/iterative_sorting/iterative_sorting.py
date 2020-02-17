# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    if len(arr) == 0:
        return []
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for k in range(i, len(arr)):              #mistake - len(arr) NOT len(arr)-1
            if arr[k] < arr[smallest_index]:
                smallest_index = k
        # TO-DO: swap
        item = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = item


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) == 0:
        return []

    for i in range(0, len(arr)-2):
        for k in range(0, len(arr)-1):
            if arr[k] > arr[k+1]:
                item = arr[k+1]
                arr[k+1] = arr[k]
                arr[k] = item

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    maximum = -1
    for i in range(0, len(arr)-1):
        if arr[i] > maximum:
            maximum = arr[i]
    
    newArr = []
    for i in range(0, maximum):
        newArr[i] = 0
    
    for i in range(0, len(arr)-1):
        newArr[arr[i]] += 1

    # for i in range(0, len(arr)-1):



    return arr

# sorting algorithm 
# counting sort = counting occurrances
# counting each item for its unique occurrances 
# maximum = number of elements from 0 to element
# make an array size maximum to track occurrances 