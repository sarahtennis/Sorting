### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
# 2. Move all elements smaller than the pivot to the left. 
# 3. Move all elements greater than the pivot to the right.
# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
def quick_sort( arr, low, high ):
    def place_pivot(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            # left travel as far right as possible
            while arr[left] < pivot and left <= right:
                left += 1

            # right travel as far left as possible
            while arr[right] > pivot and right >= left:
                right -= 1

            # once they are as far as possible...
            if left <= right:
                # if they haven't passed each other, swap them
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            else: 
                break
        
        # correctly place pivot
        arr[low] = arr[right]
        arr[right] = pivot

        # return index of correctly placed pivot
        return right

    if low < high and high <= len(arr) - 1 and low >= 0:
        pivot_index = place_pivot(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(quick_sort(arr1, 0, len(arr1)-1))

'''
[1piv, !!5, 8, 4, 2, 9, 6, 0, 3, 7!!] - move as far as possible
[1piv, !!5, 8, 4, 2, 9, 6, 0!!, 3, 7] - right > left, swap right/left
[1piv, !!0, 8, 4, 2, 9, 6, 5!!, 3, 7] - move as far as possible
[1piv, 0!!, !!8, 4, 2, 9, 6, 5, 3, 7] - left > right, swap pivot/right
[0, 1piv, 8, 4, 2, 9, 6, 5, 3, 7] - recursion on arr divided by pivot's correct index
[0piv] 1 [8piv, 4, 2, 9, 6, 5, 3, 7] - lhs is done, move rhs
0 1 [8piv, 4, 2, !!9, 6, 5, 3, 7!!] - right > left, swap right/left
0 1 [8piv, 4, 2, !!7, 6, 5, 3, 9!!] - keep moving
0 1 [8piv, 4, 2, 7, 6, 5, 3!!, !!9] - left > right, swap pivot/right
0 1 [3, 4, 2, 7, 6, 5, 8piv, 9] - recursion on arr divided by pivot's correct index
0 1 [3piv, 4, 2, 7, 6, 5] 8 [9piv] - rhs done, move lhs
0 1 [3piv, !!4, 2!!, 7, 6, 5] 8 9 - right > left, swap left/right
0 1 [3piv, !!2, 4!!, 7, 6, 5] 8 9 - keep moving
0 1 [3piv, 2!!, !!4, 7, 6, 5] 8 9 - left > right, swap pivot/right
0 1 [2, 3piv, 4, 7, 6, 5] 8 9 - recursion on arr divided by pivot's correct index
0 1 [2piv] 3 [4piv, 7, 6, 5] 8 9 - lhs done, move rhs
0 1 2 3 [4piv!!, !!7, 6, 5] 8 9 - left > right, swap pivot/right
0 1 2 3 [4piv, 7, 6, 5] 8 9 - recursion on arr divided by pivot's correct index
0 1 2 3 [] 4 [7piv, 6, 5] 8 9 - lhs low=high, move rhs
0 1 2 3 4 [7piv, 6, 5!! (!!)] 8 9 - left > right (left not index of arr), swap pivot/right
0 1 2 3 4 [5, 6, 7piv] 8 9 - recursion on arr divided by pivot's correct index
0 1 2 3 4 [5piv, 6] 7 [] 8 9 - lhs move, rhs low=high
0 1 2 3 4 [5piv!!, !!6] 7 8 9 - left > right, swap pivot/right
0 1 2 3 4 [5piv, 6] 7 8 9 - recursion on arr divided by pivot's correct index
0 1 2 3 4 5 [] [6piv] 7 8 9 - lhs low=high, rhs move
0 1 2 3 4 5 [(!!) 6piv (!!)] 7 8 9 - left > right (left/right not indices of arr), swap pivot/right
0 1 2 3 4 5 [6piv] 7 8 9 - recursion done, return array
0 1 2 3 4 5 6 7 8 9
'''


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
