# Hitesh Sharma


import math as m
class Solution:
    def sieveOfEratosthenes(self, N):
        sieve = [True for i in range(N+1)]
        
        sieve[0] = False
        sieve[1] = False
        
        n = int(m.sqrt(N))
        
        i = 2
        
        while(i*i<=N):
            if sieve[i] == True:
                for j in range(i*i, N+1,i):
                    sieve[j] = False
                    
            i+=1
            
        '''
            
        for i in range(2, n+1):
            if sieve[i] == True:
                for j in range(i*i, N+1, i):
                    sieve[j] = False
        
        arr1 = []
        for i in range(2, N+1):
            if sieve[i] == True:
                arr1.append(i)
        
        '''
        
        arr = []
        
        for i in range(2, N+1):
            if sieve[i] == True:
                arr.append(i)
        
        return arr
        
        
        
        
        #code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
