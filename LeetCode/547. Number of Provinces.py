"""
To solve **547. Number of Provinces**, we can think of the matrix as an **undirected graph**, where each city is a **node**, and a `1` in `isConnected[i][j]` means there's an **edge** between city `i` and city `j`.

---

## ✅ Problem Summary

- You are given an **adjacency matrix** for an undirected graph.
- You need to count the number of **connected components** in the graph.
- A **province** = a connected component of cities.

---

## ✅ Approach: DFS (Depth-First Search)

We'll:

1. Traverse each city.
2. If it's **unvisited**, run DFS to mark all cities in that province as visited.
3. Each DFS call that starts from an unvisited node means we found a **new province**.

"""

def findCircleNum(isConnected):
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    provinces = 0
    for city in range(n):
        if not visited[city]:
            visited[city] = True
            dfs(city)
            provinces += 1

    return provinces
