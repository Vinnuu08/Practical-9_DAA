import heapq

def prim_mst(graph, start_vertex=0):
    """
    Finds the Minimum Spanning Tree (MST) of a graph using Prim's Algorithm.
    
    :param graph: Dictionary where keys are vertices and values are lists of (neighbor, weight) tuples.
    :param start_vertex: The vertex to begin the algorithm from.
    :return: A tuple containing (list of MST edges, total weight of the MST).
    """
    # Priority queue stores tuples of: (weight, current_vertex, parent_vertex)
    # It always pops the edge with the minimum weight.
    min_heap = []
    
    # Track vertices already included in the MST
    visited = set()
    
    # Store the final edges of the MST and the accumulated weight
    mst_edges = []
    total_weight = 0
    
    # Start by pushing a dummy edge for the initial vertex with 0 weight
    heapq.heappush(min_heap, (0, start_vertex, None))
    
    while min_heap and len(visited) < len(graph):
        weight, current, parent = heapq.heappop(min_heap)
        
        # If the vertex is already in the MST, skip it to avoid cycles
        if current in visited:
            continue
            
        # Add the vertex to the MST
        visited.add(current)
        total_weight += weight
        
        # If it's not the starting vertex, record the edge
        if parent is not None:
            mst_edges.append((parent, current, weight))
            
        # Explore neighbors of the current vertex
        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))
                
    return mst_edges, total_weight

# --- Example Usage ---
if __name__ == "__main__":
    # Representing an undirected, weighted graph as an adjacency list
    # Graph structure:
    #   0 -(4)- 1,  0 -(8)- 7
    #   1 -(8)- 2,  1 -(11)- 7
    #   ... (matching a standard sample graph)
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }
    
    mst, total_cost = prim_mst(graph, start_vertex=0)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"Edge {u} - {v} with weight {w}")
        
    print(f"\nTotal Weight of MST: {total_cost}")
