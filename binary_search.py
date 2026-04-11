# A binary search O(log n)
def binary_search(arr, item):
  # low and high keep track of which part of the list you'll search in
  low = 0
  high = len(arr) - 1
  while low <= high:      # while the list hasn't been narrowed down to one element
    mid = (low + high) // 2
    print(mid)
    guess = arr[mid]

    if guess == item:
      return mid
    elif guess < item:
      low = mid + 1
    else:
      high = mid - 1
  return None 

nums = [10, 20, 30, 40, 50, 60, 70, 80]

print(binary_search(nums, 50))