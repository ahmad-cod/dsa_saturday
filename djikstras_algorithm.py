import math
# Algorithm to implement djikstra's algorithm
def find_lowest_cost_node(costs):
  pass

# while we have nodes to process
# Grab the node that is closest to the start
# update costs for its neighbours
# if any of the neighbour's costs were updated, update its parent too
# mark this node processed

graph = {
  "start": {"a": 6, "B": 2},
  "a": {},
  "b": {"a", "fin"}
}
costs = {
  "start": [6, 2]
}
parents = {}

processed = set()

node = find_lowest_cost_node(costs={})
while node is not None:
  cost = costs[node]
  neighbours = graph[node]

  for n in neighbours.keys():
    new_cost = cost + neighbours[n]
    if costs[n] > new_cost:  # if it's cheaper to get to this out-neighbour by going through this node...
      costs[n] = new_cost    # ...updates the cost for the neighbour
      parents[n] = node      # if any of the neighbour's cost was updated, update its parent too
  processed.add(node)     # Mark the node as processed
  node = find_lowest_cost_node(node)

def find_lowest_cost_nodes(costs):
  lowest_cost = math.inf
  lowest_cost_node = None
  
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node