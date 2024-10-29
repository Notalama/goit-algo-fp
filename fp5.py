from fp4 import add_edges, Node
import networkx as nx
import matplotlib.pyplot as plt

def visualize_traversal(tree_root, traversal_type='dfs'):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  add_edges(tree, tree_root, pos)

  if traversal_type == 'dfs':
    stack = [tree_root]
    order = []
    while stack:
      node = stack.pop()
      order.append(node.id)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)
  elif traversal_type == 'bfs':
    queue = [tree_root]
    order = []
    while queue:
      node = queue.pop(0)
      order.append(node.id)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
  else:
    raise ValueError("Invalid traversal type. Use 'dfs' or 'bfs'.")

  # Generate colors
  num_nodes = len(order)
  colors = ['#%02x%02x%02x' % (int(255 * (i / num_nodes)), int(255 * (i / num_nodes)), 255) for i in range(num_nodes)]

  for i, node_id in enumerate(order):
    tree.nodes[node_id]['color'] = colors[i]

  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=[tree.nodes[node]['color'] for node in tree.nodes()])
  plt.show()

# Приклад використання:
heap = [0, 4, 1, 5, 10, 3]
root = Node(heap[0])
root.left = Node(heap[1])
root.right = Node(heap[2])
root.left.left = Node(heap[3])
root.left.right = Node(heap[4])
root.right.left = Node(heap[5])

visualize_traversal(root, traversal_type='dfs')
visualize_traversal(root, traversal_type='bfs')