def quicksort(arr):
  if len(arr) < 2:
    return arr
  pivot = arr[0]
  less = [i for i in arr[1:] if i < pivot]
  greater = [i for i in arr[1:] if i > pivot]
  # but what if there were repetition of the pivot
  return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 10, 2, 3]))