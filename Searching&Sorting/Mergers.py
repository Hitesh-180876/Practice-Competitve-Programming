# Hitesh Sharma
# Merge Sort


class Solution:
    def merge(self,a, a1, a2): 
        # code here
        i = j = k = 0
        
        while i<len(a1) and j<len(a2):
            if a1[i]<=a2[j]:
                a[k] = a1[i]
                k+=1
                i+=1
            
            else:
                a[k] = a2[j]
                k+=1
                j+=1
            
        while i<len(a1):
            a[k] = a1[i]
            k+=1
            i+=1
        
        while j<len(a2):
            a[k] = a2[j]
            k+=1
            j+=1
        
            
    def mergeSort(self,arr, l, r):
        #code here
        
        n=len(arr)
        
        if len(arr) == 1:
            return arr
            
        mid = len(arr)//2
        
        a1 = arr[0:mid]
        a2 = arr[mid:]
        
        self.mergeSort(a1,0, 0)
        self.mergeSort(a2, 0, 0)
        
        return self.merge(arr, a1, a2)
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
