class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def Dfs(self, root, stack, check):
        if check[root] == False:
            print(root, end=" ")
            check[root] = True
            x = 0
            for i in range(self.V - 1, -1, -1):
                if self.graph[root][i] == 1 and check[i] == False:
                    stack.append(i)
                    x += 1
            for i in range(x):
                self.Dfs(stack.pop(), stack, check)


print("Enter the number of vertices : ")
n = int(input())
g = Graph(n)
print("Enter the number of edges : ")
e = int(input())
print(f"Notic: The name of vertices is 0 to {n - 1}.")
print("Enter edges like this format : first vertex-second vertex\nsample : 0-4")
for i in range(e):
    edges = input().split("-")
    g.graph[int(edges[0])][int(edges[1])] = 1
    g.graph[int(edges[1])][int(edges[0])] = 1

print("Enter the root vertex : ")
root = int(input())
stack = list()
check = [False for i in range(n)]
stack.append(root)
g.Dfs(root, stack, check)

if False in check:
    print("\nGraph is not Connected.")
else:
    print("\nGraph is Connected.")
