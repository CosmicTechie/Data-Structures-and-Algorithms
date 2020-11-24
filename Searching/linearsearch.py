def search(li, n, x): 
  
    for i in range(0, n): 
        if (li[i] == x): 
            return i 
    return -1
 
inp = input("Enter the list:") 
inp=inp.split()
li=[]
for i in inp:
    li.append(int(i))

x = int(input("Enter the element to be searched: "))
n = len(li) 
  
# Function call 
result = search(li, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result) 
