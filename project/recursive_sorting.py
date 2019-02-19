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
[1, !!5, 8, 4, 2, 9, 6, 0, 3!!, 7] -- 5 is greater, 0 is less so swap
[1, !!0, 8, 4, 2, 9, 6, 5!!, 3, 7] - keep moving right and left indices as possible
[1, !!0, 8!!, 4, 2, 9, 6, 5, 3, 7] -- left and right meet at 0, swap pivot and 0
[0, 1p, 8, 4, 2, 9, 6, 5, 3, 7] -- break into recursion based on final index for pivot
[0] 1 [8, 4, 2, 9, 6, 5, 3, 7] -- len([0]) = 1 so it is in position (no more recursion on left)
0 1 [8, 4, 2, !!9, 6, 5, 3, 7!!] - 9 is greater, 7 is less so swap
0 1 [8, 4, 2, !!7, 6, 5, 3, 9!!] - keep moving
0 1 [8, 4, 2, 7, 6, 5, 3!!, !!9] - right < left, swap pivot with right
0 1 [3, 4, 2, 7, 6, 5, 8p, 9] - recursion
0 1 [3, 4, 2, 7, 6, 5] 8 [9] - len([9]) = 1 stop recursion on right of 8
0 1 [3, !!4, 2!!, 7, 6, 5] 8 9 - right > left, swap
0 1 [3, !!2, 4!!, 7, 6, 5] 8 9 - continue moving
0 1 [3, 2!!, 4!!, 7, 6, 5] 8 9 - left > right, swap pivot with right
0 1 [2, 3p, 4, 7, 6, 5] 8 9 - recursion
0 1 [2] 3 [4, 7, 6, 5] 8 9 - len([2]) = 1, correct place
0 1 2 3 [4!!, !!7, 6, 5] 8 9 - left > right, pivot at right
0 1 2 3 [4p, 7, 6, 5] 8 9 - recursion
0 1 2 3 4 [7, 6, 5] 8 9
0 1 2 3 4 [7, 6, !!5!!] 8 9 
0 1 2 3 4 [5, 6, 7p] 8 9
0 1 2 3 4 [5, 6] 7 8 9
0 1 2 3 4 [5!!, !!6] 7 8 9
0 1 2 3 4 5 6 7 8 9
'''


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
