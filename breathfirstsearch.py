from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
# create a queue
# initialize search queue with the out neighbours of the first name
# create a set to monitor visited nodes (names)
# while search_queue is not empty
# get the first name using popleft
# check if it's not already visited
# if not visited already:
# check it against the function to determine if it's what we're looking for, here is_seller
# if it is print something and return True
# else:
# add it's out neighbours to the search_queue
# add the name to the visited set
  search_queue = deque()
  search_queue += graph[name]
  visited = set()

  while search_queue:
    person = search_queue.popleft()
    if not person in visited:
      if is_seller(person):
        print(person + " is a mango seller")
        return True
      else:
        search_queue += graph[person]
        visited.add(person)
  print('Not Found!')
  return False

def is_seller(person: str):
  return person.endswith('m')

search('you')