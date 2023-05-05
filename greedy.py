def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            if array[i] < array[min_idx]:
                min_idx = i
      
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [2, 45, 0, 11, 9, 56, 3]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

print("-------------------------------------------")

# Prim's Algorithm in Python


INF = 9999999

V = 5

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]

no_edge = 0

selected[0] = True

print("Edge : Weight\n")
while (no_edge < V - 1):
   
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                  
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1