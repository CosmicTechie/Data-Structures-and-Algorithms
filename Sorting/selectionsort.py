def selectionSort(data):
   
    for step in range(len(data)):
        min_idx = step 

        for i in range(step + 1, len(data)):
         
            if data[i] < data[min_idx]: #Reversing the comparison operator will result in descending order sort 
                min_idx = i
         
        (data[step], data[min_idx]) = (data[min_idx], data[step])
        print("Step",step+1,"--",data)

inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))
selectionSort(data)
print('Sorted list in Ascending Order:')
print(data)
