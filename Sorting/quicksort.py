def partition(array,low,high): 
    i = ( low-1 )         # Index of smaller element 
    pivot = array[high]     # Pivot Value
  
    for j in range(low , high): 
  
        if   array[j] < pivot:         # If current element is smaller than the pivot 
        
            i = i+1             # Increment index of smaller element 
            array[i],array[j] = array[j],array[i]   
    array[i+1],array[high] = array[high],array[i+1] 
    return ( i+1 ) 


def quickSort(array, low, high):
    if low < high:

        # Select pivot position and put all the elements smaller than pivot on left and greater than pivot on right
        pi = partition(array, low, high)

        # Sort the elements on the left of pivot
        quickSort(array, low, pi - 1)

        # Sort the elements on the right of pivot
        quickSort(array, pi + 1, high)

inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
quickSort(data, 0, len(data) - 1)
print('Sorted list in Ascending Order:')
print(data)
