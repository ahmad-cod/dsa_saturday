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