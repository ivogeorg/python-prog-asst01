# Python program for implementation of Bubble Sort
# Acknowledgement: GeeksforGeeks

# Note: The matching array and function argument
# names 'arr', as well as the same loop variable
# names 'i' for loops in the global and function
# scopes, are left in to demonstrate and explain
# shadowing.


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]



bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
