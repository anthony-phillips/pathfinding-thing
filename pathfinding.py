graph = []
start_node = ()
goal_node = ()
visited = []
path = []

# Heuristic function
def manhattan(n):
   return abs(n[0]-goal_node[0]) + abs(n[1]-goal_node[1])

# Successor function, returns the children of a parent
# ordered by increasing cost estimated by heuristic
def children(parent, grandparent):
   valid_dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)] # The valid moves from parent node
   children = []
   for dxdy in valid_dxdy:
      child_x = parent[0] + dxdy[0]
      child_y = parent[1] + dxdy[1]
      child = (child_x, child_y)
      if child_x < 0 or child_x == len(graph): # If child is not in graph
         continue
      if child_y < 0 or child_y == len(graph[child_x]): # If child is not in graph
         continue
      if child in visited: # A wee bit exhaustive but prevents revisited states
         continue
      if graph[child_x][child_y] is not 'X': # If child is not a wall, it can be expanded
            children.append(child)

   # Sort the children based on their heuristic
   children.sort(key=lambda child: manhattan(child))

   return children

def expand(n, grandparent):
   visited.append(n) # add this to the list of visited nodes
   if n == goal_node: # goal check
      return True

   fringe = children(n, grandparent) # generate the children (sorted by heuristic)

   if not fringe: # if there are no moves from here, go back
      return False

   for fringe_node in fringe: # else go through the children
      if expand(fringe_node, n):
         path.append(fringe_node)
         return True
   
print('Enter a graph')
print('Enter \'Y\' when finished')

x = 0
while (True):
   user_input = input()

   if user_input == 'Y': break

   y = 0
   for char in user_input:
      if char == 'S':
         start_node = (x, y)
      elif char == 'G':
         goal_node = (x, y)
      y += 1

   graph.append(user_input)
   x += 1

if not expand(start_node, start_node):
      print('No path found.')
path.append(start_node)
path.reverse()
print(path)
