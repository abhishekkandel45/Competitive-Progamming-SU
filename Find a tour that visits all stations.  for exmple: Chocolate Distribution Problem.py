class Solution: 
    def Countpair(self, arr, n, sum):
        # function to count pairs with sum equal to X

        # code here
        i=0
        j=len(arr)-1
        count=0
        while(i < j):
            
            if arr[i]+arr[j]==sum:
                count=count+1
                
            if arr[i]+arr[j] >sum:
                j = j-1
            else:
                i=i+1
                
        res= count if count!=0 else -1  # Creating ternary operator in python
        
        return res
