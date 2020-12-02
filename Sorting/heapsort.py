def heapify(data, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    # Check if left child of root exists and is greater than root
    if l < n and data[largest] < data[l]:
        largest = l
 
    # Check if right child of root exists and is greater than root
    if r < n and data[largest] < data[r]:
        largest = r
 
    # If needed, Change the root
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  #Swap
 
        heapify(data, n, largest)   # Heapify Root.

def heapSort(data):
    n = len(data)
 
    # Building MaxHeap.
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i)
 
    # Extract elements one by one
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]  #Swap
        heapify(data, i, 0)
 
 
inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
heapSort(data)
n = len(data)
print("Sorted List is")
print(data)
