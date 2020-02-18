# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] == arrB[j]:
            merged_arr.append(arrA[i])
            merged_arr.append(arrB[j])
            i += 1
            j += 1
        elif arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        elif arrB[j] < arrA[i]:
            merged_arr.append(arrB[j])
            j += 1
    
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    # print(merged_arr)
    return merged_arr

print(merge([1, 1, 2, 3, 5, 8, 9], [2, 2, 4, 5, 9, 10, 11]))





# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr 

    midpoint = len(arr) // 2
    left = arr[0: midpoint]
    right = arr[midpoint: ]

    return merging(merge_sort(left), merge_sort(right))


def merging(left, right):
    newArr = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            newArr.append(left[0])
            left = left[1:]

        elif left[0] > right [0]:
            newArr.append(right[0])
            right = right[1:]
    
    while len(left) > 0:
        newArr.append(left[0])
        left = left[1:]

    while len(right) > 0:
        newArr.append(right[0])
        right = right[1:]

    return newArr

print(merge_sort([1, 5, 9, 3, 2, 8, 9]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
