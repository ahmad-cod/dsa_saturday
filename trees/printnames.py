from os import listdir
from os.path import isfile, join

def printnames(dir: str):
  """
  this function uses recursion (Depth First Search) 
  to print the names of all files in a dir and its sub-dirs
  """
  for file in sorted(listdir(dir)):
    fullpath = join(dir, file)
    if isfile(fullpath):
      print(file)
    else:
      printnames(fullpath)

printnames("/home/aroyehun/Documents")
