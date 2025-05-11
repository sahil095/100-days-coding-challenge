"""
## ✅ 1. **Most Common Solution** — **Convert to Graph + BFS**

### 🧠 Intuition:

- In a binary tree, we can easily go **downward** (to left/right children) — but not **upward** (to parent).
- To solve this problem efficiently:
    1. First, **convert the tree into an undirected graph** — this lets us move both ways.
    2. Then, **run BFS** from the target node to find all nodes at distance `k`.

---

### 👨‍💻 Step-by-Step Plan:

1. Build a `graph: node_val -> list of connected node_vals`
2. Create a visited set
3. Do BFS starting from `target` for `k` levels
4. Return nodes at that level

"""

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Build the graph
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: BFS from target.val
        visited = set()
        queue = deque([(target.val, 0)])
        visited.add(target.val)
        result = []

        while queue:
            node_val, dist = queue.popleft()
            if dist == k:
                result.append(node_val)
            elif dist < k:
                for neighbor in graph[node_val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result
