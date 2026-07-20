"""
Reverse an Array (Naukri Code360) - recursive, two-pointer, in-place
Reverse the order of elements in an array using recursion.
Striver A2Z - Step 1: Basics
Key idea: pass the SAME array with shrinking index bounds (left, right)
instead of slicing -- slicing creates disconnected copies whose
mutations never make it back to the original array.
"""

def reverseArray(arr, left, right):
    if left >= right:
        return arr
    else:
        arr[left], arr[right - 1] = arr[right - 1], arr[left]
        reverseArray(arr, left + 1, right - 1)
    return arr

if __name__ == "__main__":
    print(reverseArray([1, 2, 3, 4, 5], 0, 5))          # [5,4,3,2,1]
    print(reverseArray([1, 2, 3, 4, 5, 6], 0, 6))        # [6,5,4,3,2,1]
    print(reverseArray([7], 0, 1))                        # [7]
    print(reverseArray([], 0, 0))                          # []
