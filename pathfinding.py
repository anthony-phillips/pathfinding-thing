graph = []
start_node = ()
goal_node = ()
path = []

# Heuristic function
def manhattan(n):
   return abs(n[0]-goal_node[0]) + abs(n[1]-goal_node[1])

# Successor function, returns the children of a parent
# ordered by increasing cost estimated by heuristic
def children(parent):
   children = []

   # Generate all possible children
   for dx in range(-1, 1):
      for dy in range(-1, 0):
         child_x = abs(parent[0] - dx)
         child_y = abs(parent[1] - dy)
         child = graph[child_x][child_y]
         if (not child): # If child is 0, it can be expanded
            children.append((child_x, child_y, manhattan))
   
   # Order the children based on their heuristic
   children.sort(key=lambda tup: tup[2])

   return []

def expand(n):
   path.append(n)

   fringe = children(n)

   if (not fringe):
      path.pop()
      return False

   for fringe_node in fringe:
      if (expand(fringe_node)):
         path.append(fringe_node)

   if (n == goal_node): # goal check
      return True
   
print('Enter a graph')
print('Enter \'Y\' when finished')

y = 0
while (True):
   user_input = input()

   if (user_input == 'Y'): break

   x = 0
   for char in user_input:
      if (char == 'S'):
         start_node = (x, y)
      elif (char == 'G'):
         goal_node = (x, y)
      x += 1

   graph.append(user_input)
   y += 1

expand(start_node)

print(graph)
print(start_node)
print(goal_node)
print(manhattan(start_node))
