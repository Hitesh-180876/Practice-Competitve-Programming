''' Quick Sort using python

'''


class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        
        if low >= high:
            return 
        
        c = self.partition(arr, low, high)
        
        self.quickSort(arr, low, c-1)
        self.quickSort(arr, c+1, high)
        # code here
        
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[low]
        
        count = 0
        for i in range(low, high+1):
            
            if arr[i] < pivot:
                count+=1
        
        arr[low+count], arr[low] = arr[low], arr[low+count]
        
        pivotIndex = low+count
        
        
        i = low 
        j = high
        
        while i<j:
            if arr[i]<pivot:
                i+=1
            elif arr[j]>=pivot:
                j = j-1
                
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j = j-1
            
        return pivotIndex
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
