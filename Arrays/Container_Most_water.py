#Container With Most Water
# Time complexity o(n) using two pointer technique

def maxArea(height):
    l = 0
    r = len(height) -1 
    maxArea = 0

    while (l < r):
        #Calculate area by taking a diff in two pointers multiply by lowest element between two
        curr_area = (r-l) * min(height[l],height[r])
        print(curr_area)
        if curr_area > maxArea:
            maxArea = curr_area
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    print(maxArea)        
    return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maxArea(height)


