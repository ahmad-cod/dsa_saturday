scores = [
  ['ihsan', 99],
  ['savvy', 34],
  ['artemis', 89]
]
ages = [2, 34, 54, 12, 19]
def selection_sort(arr):
  result = []
  for a in range(len(arr)):
    max = arr[0][1]
    max_index = 0
    for i in range(1, len(arr)):
      if max < arr[i][1]:
        max = arr[i][1]
        max_index = i
    result.append(arr.pop(max_index))
    # arr.remove(arr[max_index])
  return result

print(selection_sort(scores))

def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if smallest > arr[i]:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selection_sort(arr):
  result = []
  copied_arr = arr[:]       # Create a copy of the original array to avoid modifying it
  for i in range(len(copied_arr)):
    smallest_index = find_smallest(copied_arr)
    result.append(copied_arr.pop(smallest_index))
  return result

print(selection_sort([5, 3, 6, 2, 10]))
print(selection_sort(ages))