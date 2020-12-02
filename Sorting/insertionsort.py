def insertionSort(data):

    for step in range(0, len(data)):
        key = data[step]
        j = step - 1
        
        while j >= 0 and key < data[j]:   # Change key<data[j] to key>data[j] for descending order.        
            data[j + 1] = data[j]
            j = j - 1
        
        data[j + 1] = key
        print("step",step," -- ",data)
inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
insertionSort(data)
print('Sorted list in Ascending Order:')
print(data)
