# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for index, element in enumerate(arr):
    if element == target:
      return index
  return -1   # not found

# STRETCH: write an iterative implementation of Binary Search
# Compare the item in the middle of the data set to the item we are searching for.
#   If it is the same, stop. We found it and are done!
#   Else, if the item we are searching for is LESS than the item in the middle:
#     Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
#   Else, the item we are searching for is GREATER than the item in the middle:
#     Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.

def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  mid = (len(arr) - 1) // 2
  high = len(arr) - 1

  # TO-DO: add missing code
  while high != low:
    if arr[mid] > target:
      high = mid
      mid = (high - low) // 2
    elif arr[mid] < target:
      low = mid
      mid = (high - low) // 2
    else:
      return mid

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low = 0, high = None):
  if not high:
    high = len(arr) - 1
  
  middle = (low+high) // 2

  if len(arr) == 0:
    return -1 # array empty

  if arr[middle] >  target:
    return binary_search_recursive(arr, target, low, middle)
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle, high)
  else:
    return middle
  # TO-DO: add missing if/else statements, recursive calls
