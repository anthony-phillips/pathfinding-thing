from heuristics import *
from time import clock

graph = []
start_node = ()
goal_node = ()
visited = []
path = []
num_visited = 0

def main():
   global num_visited
   global goal_node
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

      graph.append(list(user_input))
      x += 1

   print('Depth-first:')
   start = clock()
   found = expand(start_node)
   end = clock()
   if not found:
         print('No path found.')
   print('Time: ' + str(end - start))
   print('Visited Nodes: ' + str(len(visited)))
   print_path()
   visited.clear()
   path.clear()

   print('Depth-first Manhattan Heuristic:')
   start = clock()
   found = expand(start_node, manhattan)
   end = clock()
   if not found:
         print('No path found.')
   print('Time: ' + str(end - start))
   print('Visited Nodes: ' + str(len(visited)))
   print_path()
   visited.clear()
   path.clear()

   print('Depth-first Euclidean Heuristic:')
   start = clock()
   found = expand(start_node, euclidean)
   end = clock()
   if not found:
         print('No path found.')
   print('Time: ' + str(end - start))
   print('Visited Nodes: ' + str(len(visited)))
   print_path()
   visited.clear()
   path.clear()

def print_path():
   cell_width = len(str(len(path)-2)) + 1
   solved_graph = [ [str(cell).center(cell_width, ' ') for cell in row] for row in graph ]
   for i in range(1, len(path)-1):
      x = path[i][0]
      y = path[i][1]
      solved_graph[x][y] = str(i).center(cell_width, ' ')

   for row in solved_graph:
      print(''.join(row))

# Successor function, returns the children of a parent
# ordered by increasing cost estimated by heuristic
def successors(parent):
   valid_dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)] # The valid moves from parent node
   successors = []
   for dxdy in valid_dxdy:
      child_x = parent[0] + dxdy[0]
      child_y = parent[1] + dxdy[1]
      child = (child_x, child_y)
      if child_x < 0 or child_x >= len(graph): # If child is not in graph
         continue
      if child_y < 0 or child_y >= len(graph[child_x]): # If child is not in graph
         continue
      if child in visited: # A wee bit exhaustive but prevents revisited states
         continue
      if graph[child_x][child_y] not in ['X', ' '] : # If child is not a wall / off the graph, it can be expanded
            successors.append(child)
   return successors

def expand(current, heuristic=None):
   visited.append(current) # add this to the list of visited nodes
   path.append(current)
   if current == goal_node: # goal check
      return True

   fringe = successors(current) # generate the children and put into the fringe for this node

   if heuristic:
      fringe.sort(key=lambda n: heuristic(n, goal_node))  # sort the fringe by heuristic
 
   for fringe_node in fringe: # dive down the children in order of most promising to least
      if expand(fringe_node, heuristic):
         return True

   path.remove(current)
   return False

if __name__ == '__main__':
   main()
