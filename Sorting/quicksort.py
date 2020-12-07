def partition(data,low,high): 
    i = ( low-1 )         # Index of smaller element 
    pivot = data[high]     # Pivot Value
  
    for j in range(low , high): 
  
        if   data[j] < pivot:         # If current element is smaller than the pivot 
        
            i = i+1             # Increment index of smaller element 
            data[i],data[j] = data[j],data[i]   
    data[i+1],data[high] = data[high],data[i+1] 
    return ( i+1 ) 


def quickSort(data, low, high):
    if low < high:

        # Select pivot position and put all the elements smaller than pivot on left and greater than pivot on right
        pi = partition(data, low, high)

        # Sort the elements on the left of pivot
        quickSort(data, low, pi - 1)

        # Sort the elements on the right of pivot
        quickSort(data, pi + 1, high)

inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
quickSort(data, 0, len(data) - 1)
print('Sorted list in Ascending Order:')
print(data)
