import math as m
class Solution:
    def isPrime (self, N):
        # code here
        
        n = int(m.sqrt(N))
        count = 0
        for i in range(1, n+1):
            if N%i == 0:
                if i*i == N:
                    count+=1
                else:
                    count+=2
        
        if count>2 or count<2:
            return 0
        
        else:
            return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends
