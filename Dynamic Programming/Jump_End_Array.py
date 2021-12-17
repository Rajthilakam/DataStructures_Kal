# Program to find if possible to reach the end of the array


arr = [1,1,1,0,3]


def jump(arr):
    maxlocation = 0
    for i in range(len(arr)):
        if maxlocation < i:
            return False
        # Calculating maxlocation by taking the max of index,correspondingvalue and previous maxlocation   
        maxlocation = max(i+arr[i],maxlocation)
        #print(maxlocation)
    return True
        
jump(arr)        