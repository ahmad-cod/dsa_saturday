import math

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}     # The finish node doesn't have any out-neighbours

print(list(graph["start"].keys()))

# We need a hash table to stare the current costs for each node

infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# We also need another hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Finally, we need a set to keep track of all the nodes we've already processed
# because we don't need to process a node more than once:
processed = set()
