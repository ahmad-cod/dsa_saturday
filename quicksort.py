def quicksort(arr):
  # Pick one number -> Put it in its right position -> repeat on the left and right sub-arrays
  """
  Pick one number as the pivot, and partition the rest of the numbers into two sub-arrays, according to whether they are less than or greater than the pivot. Then recursively apply the same logic to the sub-arrays.
  """
  if len(arr) < 2:
    return arr
  pivot = arr[0]
  less = [i for i in arr[1:] if i < pivot]
  greater = [i for i in arr[1:] if i >= pivot]
  return quicksort(less) + [pivot] + quicksort(greater)
  # what if there were repetition of the pivot? We can add an "equal" list to handle that case or have it like above with >= in the greater list comprehension. The above code will work fine with duplicates as well.
  # equal = [i for i in arr if i == pivot]
  # return quicksort(less) + equal + quicksort(greater)

print(quicksort([10, 5, 10, 2, 2, 4, 8, 11, 5, 3]))

# Quicksort using inplace partition
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1        # return pivot index

def _quicksort_recursive(arr, low, high):
  if low < high:
    pivot_index = partition(arr, low, high)
    _quicksort_recursive(arr, low, pivot_index - 1)
    _quicksort_recursive(arr, pivot_index + 1, high)
  # return arr        # Uncomment to return the arr directly from the quicksort algorithm

def quicksort(arr):
  return _quicksort_recursive(arr, 0, len(arr) - 1)

print("Quicksort using inplace partition")
nums = [10, 5, 10, 2, 2, 4, 8, 11, 5, 3]

# print(quicksort(nums))
print(nums)