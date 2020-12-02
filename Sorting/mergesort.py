def mergeSort(data):
    if len(data) > 1:

        mid = len(data)//2 #point where the list is divided into two sublists
        L = data[:mid]
        R = data[mid:]

        mergeSort(L) #sorting first half
        mergeSort(R) #sorting second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1


inp=input("Enter the data: ").split()
data=[]
for i in inp:
    data.append(int(i))

mergeSort(data)

print("Sorted List is: ")
print(data)
