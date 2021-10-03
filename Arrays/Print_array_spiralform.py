#Given a 2D array, print it in spiral form. See the following examples.
# input [[1,2,3,4],[5,6,7,8][9,10,11,12]]
#output 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
#Time Complexity o(m*n)

def Print_Spiral(arr,row,column):
    top= 0
    bottom = row-1
    right = column-1
    left = 0
    dir = 0

    while(left<=right and top<=bottom):
        if(dir == 0):
            for i in range(left,right+1):
                print(arr[top][i],end=' ')
            top+=1

        if(dir == 1):
            for i in range(top,bottom+1):
                print(arr[i][right],end=' ')
            right-=1

        if(dir == 2):
            for i in range(right,left-1,-1):
                print(arr[bottom][i],end=' ')
            bottom-=1

        if(dir == 3):
            for i in range(bottom,top-1,-1):
                print(arr[i][left],end=' ')
            left+=1      
        dir = (dir+1)%4

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
row = len(arr)
column = len(arr[0])
Print_Spiral(arr,row,column)




