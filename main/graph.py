import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def generate_points(count: int) -> np.array:

    np.random.seed(20210423)
    size = 100
    xs = np.array([])
    ys = np.array([])
    for i in range(count):
        point = np.random.rand(2) * 100
        x, y = point
        xs = np.concatenate((xs.T, [x]))
        ys = np.concatenate((ys.T, [y]))
    return np.array([xs, ys])

class Graph:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = {v:[] for v in V}
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for point in self.adj[v]:
            if visited[point] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, point, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        # self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = {}
        cc = []
        for point in self.V:
            visited[point] = False
        for v in self.V:
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
 
def get_connected_components(points: np.array):
    points = [(x, y) for x, y in points.T]
    g = Graph(points)
    for pt1 in points:
        for pt2 in points:
            if pt1 == pt2:
                continue
            dist = np.linalg.norm(np.array(pt1)-np.array(pt2))
            if dist <= 10:
                g.addEdge(pt1, pt2)
    cc = g.connectedComponents()
    cc = [[np.array(pt) for pt in pts] for pts in cc]
    return cc

 
# Driver Code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    points = generate_points(50)
    points = [(x, y) for x, y in points.T]
    g = Graph(points)
    for pt1 in points:
        for pt2 in points:
            if pt1 == pt2:
                continue
            dist = np.linalg.norm(np.array(pt1)-np.array(pt2))
            if dist <= 5:
                g.addEdge(pt1, pt2)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
 
# This code is contributed by Abhishek Valsan