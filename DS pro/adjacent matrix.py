import sys
class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


print("Enter the number of vertices : ")
n = int(input())
if n==1 :
    print([0])
    sys.exit()
g = Graph(n)
vertices = []
for i in range(n):
    print(f"Enter {i + 1}st vertex:")
    vertices.append(input())
while True:
    print("Enter the number of edges : ")
    e = int(input())
    if e<= n*(n-1)/2 :
        break
    print("you enter more than maximum size of edges")
print(f"Enter edges like this format : first vertex-second vertex\nsample : {vertices[0]}-{vertices[1]} ")
for i in range(e):
    edges = input().split("-")
    if edges[0] in vertices and edges[1] in vertices:
        g.graph[vertices.index(edges[0])][vertices.index(edges[1])] = 1
        g.graph[vertices.index(edges[1])][vertices.index(edges[0])] = 1
    else:
        print("Wrong!"
              "Enter correct vertices.")
        i -= 1
for i in range(n):
    print((g.graph[i]))
