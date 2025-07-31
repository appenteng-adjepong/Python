def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x is pivot]
    right = [x for x in array if x > pivot]
    sorted_array = quicksort(left) + middle + quicksort(right)
    return sorted_array

y = [2,3,1,4,5,3,6,2,6,3,2]
print(quicksort(y))