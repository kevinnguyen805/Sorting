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

def count_sort(arr, maximum=-1):
    size = len(arr)
    
    """ find the largest element in the array """
    maximum = -1
    for i in range(0, size-1):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
    
    """ initialize counting array (with unique characters) and  """
    output = [0] * size   #len(arr) 
    count_arr = [0] * (maximum+1)

    """ get frequency of each unique character stored in its respective index"""
    for i in range(0, size):
        count_arr[arr[i]] += 1
    
    """ find cumulative sum """   
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    """ starting from the back,  """
    i = size - 1
    while i >= 0:
        output[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1
        i -= 1
    
    for i in range(0, size):
        arr[i] = output[i]
    
    return arr

