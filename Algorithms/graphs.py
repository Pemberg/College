import heapq
import tkinter as tk
from tabulate import tabulate

class Graph:
    def __init__(self):
        self.nodes = {} # Dictionary storing graph vertices and their neighbors

    def add_node(self, node):
        self.nodes[node] = {} # Adding a node to the graph

    def add_edge(self, node1, node2, weight):
        self.nodes[node1][node2] = weight # Adding edges between vertices
        self.nodes[node2][node1] = weight # Adding edges in the opposite direction (undirected graph)

    def get_neighbors(self, node):
        return self.nodes[node] # Returns neighbors of a given vertex

    def dijkstra_with_visited(self, start_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0 # Initialize distance for the starting vertex as 0

        visited = set()
        visited_nodes = []  # List of visited vertices
        queue = [(0, start_node)]

        while queue:
            current_distance, current_node = heapq.heappop(queue) # Getting the vertex with the smallest priority

            if current_node in visited:
                continue # If the vertex has already been visited, move to the next iteration

            visited.add(current_node) # Adding the current vertex to the set of visited vertices
            visited_nodes.append(current_node)  # Adding the current vertex to the list of visited vertices

            for neighbor, weight in self.get_neighbors(current_node).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor)) # Adding the neighbor to the queue with a new priority

        return distances, visited_nodes # Returns distances and visited vertices for a given starting vertex

    def calculate_all_paths(self):
        all_paths = {}

        for node in self.nodes:
            paths, visited_nodes = self.dijkstra_with_visited(node)
            all_paths[node] = (paths, visited_nodes) # Calculating the shortest paths for each vertex

        return all_paths # Returns a dictionary containing the shortest paths and visited vertices for each vertex

# Creating a graph
graph = Graph()
graph.add_node('a')
graph.add_node('b')
graph.add_node('c')
graph.add_node('d')
graph.add_node('e')
graph.add_node('f')
graph.add_node('g')
graph.add_edge('a', 'b', 5)
graph.add_edge('a', 'g', 5)
graph.add_edge('b', 'c', 3)
graph.add_edge('b', 'd', 3)
graph.add_edge('b', 'g', 5)
graph.add_edge('c', 'd', 1)
graph.add_edge('d', 'e', 5)
graph.add_edge('d', 'f', 4)
graph.add_edge('d', 'g', 3)
graph.add_edge('e', 'f', 2)
graph.add_edge('f', 'g', 5)

# Calculating the shortest paths for each vertex
all_paths = graph.calculate_all_paths()

# Results list
results = []

# Generating results
for start_node, (paths, visited_nodes) in all_paths.items():
    shortest_paths = []
    visited = set()
    for node, distance in paths.items():
        if node != start_node and node not in visited:
            shortest_paths.append([start_node, node, distance])
            visited.add(node)
    results.append([f"Shortest paths from node {start_node}:", "", ""])
    results.extend(shortest_paths)
    results.append(["Visited nodes from node " + start_node + ":",  ", ".join(visited_nodes), ""])
    results.append(["", "", ""])

# Splitting the table into two parts
half_length = len(results) // 2
table1 = results[:half_length]
table2 = results[half_length:]

# Creating a new window
window = tk.Tk()
window.title("Results")

# Creating a label with the results table (part 1)
table1_text = tabulate(table1, headers=["Starting Nodes", "Nodes Entered", "Distance"], tablefmt="fancy_grid")
label1 = tk.Label(window, text=table1_text, font=("Courier New", 8), justify="left")
label1.pack(side="left", padx=5, pady=5)

# Creating a label with the results table (part 2)
table2_text = tabulate(table2, headers=["Starting Nodes", "Nodes Entered", "Distance"], tablefmt="fancy_grid")
label2 = tk.Label(window, text=table2_text, font=("Courier New", 8), justify="left")
label2.pack(side="right", padx=5, pady=5)

# Adjusting window size to content
window.update_idletasks()
window_width = label1.winfo_width() + label2.winfo_width() + 30
window_height = max(label1.winfo_height(), label2.winfo_height()) + 20
window.geometry(f"{window_width}x{window_height}")

# Displaying the split table in a new window
window.mainloop()
