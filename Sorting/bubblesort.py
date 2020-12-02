def bubbleSort(data):
    
    for i in range(len(data)): 
        for j in range(0, len(data) - i - 1):

            if data[j] > data[j + 1]: #Reversing the comparison operator will result in descending order sort
                
                (data[j], data[j + 1]) = (data[j + 1], data[j]) #Swap 


inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
bubbleSort(data)
print('Sorted List: ')
print(data)
