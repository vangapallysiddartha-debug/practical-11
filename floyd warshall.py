
INF = float('inf')

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix (use 999 for infinity):")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 999:
            graph[i][j] = INF


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )


print("\nShortest distance matrix:")
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(int(graph[i][j]), end=" ")
    print()

