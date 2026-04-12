# a countdown function
def countdown(i):
  print(i)
  if i <= 1 :
    return
  countdown(i-1)

# countdown(5)

nums = [1000, 5, 300, 10, 990]
empty_arr = []

# calculate the sum of all numbers in a list using recursion

def sum(arr):
  size = len(arr)
  if size == 1 :
    return arr[0]
  if size == 0 :
    return 0
  return arr[0] + sum(arr[1 : size])
# print(sum(nums))
# print(sum(empty_arr))

def _sum_recursive(arr, index):
  # Base case: if we've reached the end of the array, return 0
  if index == len(arr):
    return 0
  # Add the current number to the sum of the REST of the array
  return arr[index] + _sum_recursive(arr, index + 1)

# Clean Wrapper function for the user
def sum_array(arr):
  return _sum_recursive(arr, 0)

# Test:
balances = [100, 200, 300]
print(sum_array(balances))

# Count the number of items in a list
def count(arr):
  if not arr:
    return 0
  return 1 + count(arr[1:])

# The "Walk Off the Cliff" Method (Try/Except)
# EAFP ("Easier to Ask for Forgiveness than Permission")
def _count_recursive(arr, index):
  try:
    arr[index]
    return 1 + _count_recursive(arr, index + 1)
  except IndexError:
    return 0        # Base case: Thera are no more items

# The "Iterator" Method
def _count_iterator(iterator):
  if next(iterator, None) is None:
    return 0        # Base case: no more items
  return 1 + _count_iterator(iterator)

def count(arr):
  return _count_iterator(iter(arr))
  # return _count_recursive(arr, 0)

print("Count the number of items in a list")
print(count(nums))
print(count(empty_arr))

# find the maximum number in a list of numbers
def max_number(arr):
  size = len(arr)
  max = arr[0]
  if size == 1 :
    return arr[0]
  if size == 0 :
    return 0
  
  next_max = max_number(arr[1:size])
  if max < next_max :
    max = next_max
  return max

print(max_number(nums))

def _binary_search_recursive(arr, target, left, right):
  # Base case: if the pointers cross, the target is not in the arr
  if left > right:
    return -1
  
  # Calculate mid
  # Note: We use `eft + (right - left) // 2` instead of `(left + right) // 2`
  # which are mathematically the same
  # In Python, integers don't overflow, but in Java / C++ `left+right` can
  # exceed the max integer limit. 
  # A Standard 32-bit integer can only hold values btw -2^31 and 2^31 - 1.
  # In plain numbers, the absolute maximum positive value an integer can hold is
  # 2,147,483,647

  mid = left + (right - left) // 2

  # Found it!
  if arr[mid] == target:
    return mid
  
  # Target is in the right half, move the left pointer
  if arr[mid] < target:
    return _binary_search_recursive(arr, target, mid + 1, right)
  
  # Target is in the left half, move the right pointer
  else:
    return _binary_search_recursive(arr, target, left, mid - 1)

# The "Wrapper" Function  
# We use a wrapper so the user doesn't have to manually pass `0` and `len(arr) - 1`
def binary_search(arr, target):
  if not arr:     # Handle empty list edge case
    return -1
  return _binary_search_recursive(arr, target, 0, len(arr) - 1)
  
print('Binary search result:')
print(binary_search([1,2,3,4,5,6], 5))
    