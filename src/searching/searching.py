# STRETCH: implement Linear Search				
def linear_search(arr, target):
  if len(arr) == 0:
    return -1

  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if target == arr[i]:
      return i 

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while high > low:
    midpoint = high + low // 2
    if target == arr[midpoint]:
      return midpoint 
    elif arr[midpoint] > target:
      high = midpoint-1
    elif arr[midpoint] < target:
      low = midpoint + 1
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if low > high:
    return middle
  if target == arr[middle]:
    return middle 
  elif target > arr[middle]:
    low = middle+1        #make sure you are changing the lower interval when target is higher than midpoint
    return binary_search_recursive(arr, target, low, high)
  elif target < arr[middle]:
    high = middle-1      #make sure you are changing the higher interval when target is lower than midpoint 
    return binary_search_recursive(arr, target, low, high)

