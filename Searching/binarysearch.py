def binarySearch (li, low, high, x): # Returns index of element in li if present, else -1
    
    if high >= low: 
        mid = low + (high - low) // 2
   
        if li[mid] == x:    #if element is present at mid
            return mid 
          
        elif li[mid] > x:  #If element is smaller than element at mid
            return binarySearch(li, low, mid-1, x)  # Element can only be present in left sub part of the li
  
        else: 
            return binarySearch(li, mid + 1, high, x)  #Else the element can only be present in right sub part of the li 
        
    else:  
        return -1 #Element not present in li

    
inp=input("Enter a sorted list: ").split()
li=[]
for i in inp:
    li.append(int(i))
x = int(input("Element to be Searched: "))
  
# Function call 
result = binarySearch(li, 0, len(li)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in the list") 

