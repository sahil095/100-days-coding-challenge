"""
## ✅ Step-by-Step BFS Approach (Meta Interview Style)

**Interviewer:** Return the right-side view of a binary tree — i.e., nodes you can see if you look at the tree from the right.

**Me (Candidate):**

Sure, I’d approach this using **level-order traversal (BFS)**, which naturally aligns with the concept of processing the tree layer by layer — perfect for identifying the rightmost node at each level.

1. I’ll do a typical BFS traversal using a queue.
2. For each level:
    - I’ll process all nodes at that level.
    - The **last node** I process in that level is the one that would be visible from the right.
3. I’ll add that last node’s value to the result list.

This ensures **top-to-bottom** and **rightmost at each level**.

---

## ❓ Questions I Could Ask the Interviewer

1. Is the tree always a binary tree?
2. What should we return if the tree is empty? (assume empty list)
3. Are duplicate node values allowed?
4. Do we care about memory optimization or time sensitivity?

---

## 📘 Pattern Used

- **Breadth-First Search (BFS)**
- **Level Order Traversal with focus on last node per level**

"""


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            rightmost = None

            for i in range(level_size):
                node = queue.pop(0)
                rightmost = node.val  # overwrite until last node in level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(rightmost)  # last node seen from the right

        return result
