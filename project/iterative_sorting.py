# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j    
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below

# Separate the first element from the rest of the array. Think about it as a sorted list of one element.
# For all other indices, beginning with [1]:
# a. Copy the item at that index into a temp variable
# b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
# Shift items over to the right as you iterate
# c. When the correct index is found, copy temp into this position

def insertion_sort( arr ):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break

    return arr

# arr = [2,5,9,7,4,1,3,8,6]
# print(arr)
# arr = insertion_sort( arr )
# print(arr)

# STRETCH: implement the Bubble Sort function below
# repeatedly swapping the adjacent elements if they are in wrong order
def bubble_sort( arr ):

    for i in range(len(arr)):
        swapped = False

        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swapped = True
        
        if not swapped:
            return arr 

    return arr


# STRETCH: implement the Count Sort function below
# Counting sort works by iterating through the input,
# counting the number of times each item occurs,
# and using those counts to compute an item's index in the final, sorted array.
def count_sort( arr, maximum=-1 ):
    if not len(arr):
        return []

    if maximum < 0:
        maximum = max(arr) + 1

    if maximum >= 0:
        count = [0] * (maximum + 1)
    else:
        return "Error, negative numbers not allowed in Count Sort"
    
    for num in arr:
        if num >= 0:
            count[num] += 1
        else:
            return "Error, negative numbers not allowed in Count Sort"
            

    output = []
    for i in range(maximum):
        freq = count[i]
        while freq:
            output.append(i)
            freq -= 1


    return output

print(count_sort([3,2,1,4,2,2], 5))
print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7], 10))
print(count_sort([], 10))
print(count_sort([1, 5, -2, 4, 3], 5))