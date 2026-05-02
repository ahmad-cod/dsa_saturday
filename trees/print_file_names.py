from os import listdir
from os.path import isfile, join
from collections import deque

def print_file_names(start_dir):
  """
  this function uses Binary First search to 
  print the names of files in a dir, and its sub-dirs
  """
  list_queue = deque()
  list_queue.append(start_dir)

  # Pop off a folder to look through, and
  # loop through every file and folder in the folder
  # while list_queue is not empty
  while list_queue:
    dir = list_queue.popleft()
    for file in sorted(listdir(dir)):
      fullpath = join(dir, file)
      if isfile(fullpath):
        # if it's a file, print out the name
        print(file)
      else:
        # if it's a folder, add it to the queue of folders to search
        list_queue.append(fullpath)

print_file_names("/home/aroyehun/Documents")
