#Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. 
# And the rightmost element is always a leader. 
# For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

#Time complexity o(n)

def findLeaders(arr,n):
    
    max_value = arr[n-1]  
    print (max_value)  
    for i in range(n-2,-1,-1):       
        if max_value < arr[i]:       
            print (arr[i])
            max_value = arr[i]
         

arr = [16, 17, 4, 3, 5, 2]
findLeaders(arr, len(arr))